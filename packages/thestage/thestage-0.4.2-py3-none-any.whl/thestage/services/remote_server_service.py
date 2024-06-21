import os
from pathlib import Path
from typing import Optional, List, Dict

import paramiko
import typer
from paramiko.client import SSHClient
from paramiko.config import SSHConfig
from paramiko.hostkeys import HostKeys
from paramiko.sftp_client import SFTPClient
from thestage_core.entities.file_item import FileItemEntity
from thestage_core.services.filesystem_service import FileSystemServiceCore

from thestage.exceptions.remote_server_exception import RemoteServerException
from thestage.helpers.logger.app_logger import app_logger
from thestage.entities.enums.shell_type import ShellType
from thestage.i18n.translation import __

old_value: int = 0


class RemoteServerService(object):

    def __init__(
            self,
            file_system_service: FileSystemServiceCore,
    ):
        self.__file_system_service = file_system_service

    def __get_client(
            self,
            ip_address: str,
            username: str,
    ) -> Optional[SSHClient]:
        config_by_ip = None
        ssh_path = self.__file_system_service.get_ssh_path()
        ssh_config_path = ssh_path.joinpath('config')
        #ssh_config_path = Path('~/.ssh/config')
        config_path = ssh_config_path.expanduser()
        if config_path.exists():
            config = SSHConfig.from_path(config_path)
            config_by_ip = config.lookup(ip_address)
        client = SSHClient()
        try:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if config_by_ip:
                key_file_name = config_by_ip['identityfile'][0] if config_by_ip and 'identityfile' in config_by_ip and len(config_by_ip['identityfile']) > 0 else None
                client.connect(
                    hostname=ip_address,
                    username=username,
                    timeout=60,
                    allow_agent=False if key_file_name else True,
                    look_for_keys=False if key_file_name else True,
                    key_filename=key_file_name.replace('.pub', '') if key_file_name else None,
                )
            else:
                client.connect(
                    hostname=ip_address,
                    username=username,
                    timeout=60,
                )
            return client

        except Exception as ex:
            if client:
                client.close()
                typer.echo(f"Error connect to {ip_address} by {username} ({ex})")
            app_logger.error(f"Error connect to {ip_address} by {username} ({ex})")
            raise RemoteServerException(
                message=__("Error connect to remote server"),
                ip_address=ip_address,
                username=username,
            )

    @staticmethod
    def is_shell_present(
            lines: List[str],
    ) -> Optional[ShellType]:
        bash_present, sh_present = False, False
        for line in lines:
            if 'bin/bash' in line:
                bash_present = True
                break
            elif 'bin/sh' in line:
                sh_present = True

        if bash_present:
            return ShellType.BASH
        if sh_present:
            return ShellType.SH
        else:
            return None

    def get_shell_from_container(
            self,
            ip_address: str,
            username: str,
            docker_name: str,
    ) -> Optional[ShellType]:
        client: Optional[SSHClient] = self.__get_client(ip_address=ip_address, username=username)
        stdin, stdout, stderr = client.exec_command(f'docker exec -it {docker_name} cat /etc/shells', get_pty=True)
        shell = self.is_shell_present(lines=stdout.readlines())
        client.close()

        return shell

    def check_if_host_in_list_known(self, ip_address: str) -> bool:
        try:
            #os.system(f"ssh-keygen -F 34.198.189.175")
            ssh_path = self.__file_system_service.get_ssh_path()
            known_host_path = ssh_path.joinpath('known_hosts')
            if known_host_path.exists():
                host_keys = HostKeys(filename=str(known_host_path.absolute()))
                result = host_keys.lookup(ip_address)
                if result is not None:
                    return True
                else:
                    return False
        except Exception as ex:
            raise FileNotFoundError(f"Error read ssh known host file: {ex}")
        return False

    def connect_to_instance(
            self,
            ip_address: str,
            username: str,
    ):
        try:
            os.system(f"ssh {username}@{ip_address}")
        except Exception as ex:
            app_logger.error(f"Error connect to {ip_address} by {username} ({ex})")
            raise RemoteServerException(
                message=__("Error connect to remote server"),
                ip_address=ip_address,
                username=username,
            )

    def connect_to_container(
            self,
            ip_address: str,
            username: str,
            docker_name: str,
            shell: ShellType
    ):
        try:
            os.system(f"ssh -tt {username}@{ip_address} 'docker exec -it {docker_name} {shell.value}'")
        except Exception as ex:
            app_logger.exception(f"Error connect to {ip_address} by {username} ({ex})")
            raise RemoteServerException(
                message=__("Error connect to remote server"),
                ip_address=ip_address,
                username=username,
            )

    @staticmethod
    def find_path_mapping(
            directory_mapping: Dict[str, str],
            destination_path: Optional[str] = None,
    ) -> Optional[str]:

        template = destination_path if destination_path else '/public'

        if not directory_mapping:
            typer.echo(__("Can not find mapping folders"))
            raise typer.Exit(1)

        for key, value in directory_mapping.items():
            if value == template:
                return key
        return None

    def __send_one_file(
            self,
            sftp: SFTPClient,
            src_path: str,
            dest_path: str,
            file_name: str,
            file_size: [int] = 100
    ) -> bool:
        has_error = False
        try:
            with typer.progressbar(length=file_size, label=__("Copy %file_name%", {'file_name': file_name})) as progress:
                def __show_result_copy(size: int, full_size: int):
                    global old_value
                    progress.update(size - (old_value or 0))
                    old_value = size

                sftp.put(localpath=src_path, remotepath=f"{dest_path}/{file_name}", callback=__show_result_copy)
            typer.echo(__('Complete copy %file_name%', {'file_name': file_name}))
        except FileNotFoundError as err:
            app_logger.exception(f"Error put file {file_name} to container (file ot found): {err}")
            typer.echo(__("Error put file, file not found on server"))
            has_error = True
        except Exception as err2:
            typer.echo(err2)
            app_logger.exception(f"Error put file {file_name} to container: {err2}")
            typer.echo(__("Error put file, undefined server error"))
            has_error = True

        return has_error

    def __send_list_files(
            self,
            sftp: SFTPClient,
            src_item: FileItemEntity,
            dest_path: str,
    ):
        if src_item.is_file:
            file_stat = os.stat(src_item.path)
            self.__send_one_file(
                sftp=sftp,
                src_path=src_item.path,
                dest_path=dest_path,
                file_name=src_item.name,
                file_size=file_stat.st_size,
            )
        elif src_item.is_folder:
            server_dir = f"{dest_path}/{src_item.name}"
            try:
                sftp.chdir(server_dir)  # Test if remote_path exists
            except IOError:
                sftp.mkdir(server_dir)  # Create remote_path
                sftp.chdir(server_dir)
            for item in src_item.children:
                self.__send_list_files(
                    sftp=sftp,
                    src_item=item,
                    dest_path=server_dir,
                )

    @staticmethod
    def find_sftp_server_path(
            client: SSHClient,
    ) -> Optional[str]:
        stdin, stdout, stderr = client.exec_command(f'whereis sftp-server', get_pty=True)
        for line in stdout.readlines():
            pre_line = line.replace('sftp-server:', '')
            for command in pre_line.strip().split(' '):
                tmp = command.strip()
                if tmp:
                    if tmp.endswith('/sftp-server'):
                        return tmp
        return None

    def put_data_to_container(
            self,
            ip_address: str,
            username: str,
            src_path: str,
            dest_path: str,
    ):
        has_error = False
        client: Optional[SSHClient] = self.__get_client(ip_address=ip_address, username=username)
        sftp_server_path = self.find_sftp_server_path(client=client)

        if not sftp_server_path:
            typer.echo(__('No sftp server is installed on your instance'))
            raise typer.Exit(1)

        chan = client.get_transport().open_session()
        #chan.exec_command("sudo su -c /usr/lib/openssh/sftp-server")
        chan.exec_command(f"sudo su -c {sftp_server_path}")
        sftp = paramiko.SFTPClient(chan)

        try:
            files: List[FileItemEntity] = self.__file_system_service.get_path_items(src_path)
            for item in files:
                self.__send_list_files(
                    sftp=sftp,
                    src_item=item,
                    dest_path=dest_path,
                )

        except FileNotFoundError as err:
            app_logger.error(f"Error put file to container {ip_address}, {username} (file ot found): {err}")
            typer.echo(__("Error put file, file not found on server"))
            has_error = True
        finally:
            sftp.close()

        client.close()
        if has_error:
            typer.Exit(1)
