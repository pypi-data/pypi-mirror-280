from typing import Optional, List

from thestage.services.clients.thestage_api.dtos.enums.selfhosted_status import SelfHostedStatusEnumDto
from thestage.services.clients.thestage_api.dtos.enums.rented_status import RentedStatusEnumDto
from thestage.services.instance.mapper.instance_mapper import InstanceMapper
from thestage.services.instance.mapper.selfhosted_mapper import SelfHostedMapper
from thestage.services.instance.instance_service import InstanceService
from thestage.i18n.translation import __
from thestage.controllers.utils_controller import get_current_directory, base_global_check_validation

import typer


app = typer.Typer(no_args_is_help=True, help=__("Help working with instances"))

rented = typer.Typer(no_args_is_help=True, help=__("Help working with rented instances"))
self_hosted = typer.Typer(no_args_is_help=True, help=__("Help working with self hosted instances"))

app.add_typer(rented, name="rented")
app.add_typer(self_hosted, name="self-hosted")


@rented.command(name="list", help=__("Show list rented instances"))
def rented_list(
        row: int = typer.Option(
            5,
            '--row',
            '-r',
            help=__("Count row in table"),
            is_eager=False,
        ),
        page: int = typer.Option(
            1,
            '--page',
            '-p',
            help=__("Page number"),
            is_eager=False,
        ),
        statuses: List[RentedStatusEnumDto] = typer.Option(
            ["RENTED"],
            '--status',
            '-s',
            help=__("Status item (ALL - show all instances)"),
            is_eager=False,
        ),
        no_dialog: Optional[bool] = typer.Option(
            None,
            "--no-dialog",
            "-nd",
            help=__("Start process with default values, without future dialog"),
            is_eager=False,
        ),
):
    """
        List rented instances
    """
    path = get_current_directory()
    config, facade = base_global_check_validation(path=path, no_dialog=no_dialog)

    headers = [
        #'#',
        #'ID',
        'STATUS',
        'TITLE',
        'UNIQUE ID',
        'CPU TYPE',
        'CPU CORES',
        'GPU TYPE',
        'IP ADDRESS',
        'CREATED AT',
        'UPDATED AT',
    ]

    instance_service: InstanceService = facade.get_instance_service()

    typer.echo(__(
        "Start show instance list with statuses: %statuses% (You can show all statuses set up status=ALL)",
        placeholders={
            'statuses': ', '.join([item.value for item in statuses])
        }))

    if RentedStatusEnumDto.find_special_status(statuses=statuses):
        statuses = []

    instance_service.print(
        func_get_data=instance_service.get_rented_list,
        func_special_params={
            'statuses': statuses,
        },
        mapper=InstanceMapper(),
        config=config,
        headers=headers,
        row=row,
        page=page,
        no_dialog=no_dialog,
        show_index="never",
    )

    typer.echo(__("List rented done"))
    raise typer.Exit(0)


@self_hosted.command(name="list", help=__("Show list self-hosted instances"))
def self_hosted_list(
        row: int = typer.Option(
            5,
            '--row',
            '-r',
            help=__("Count row in table"),
            is_eager=False,
        ),
        page: int = typer.Option(
            1,
            '--page',
            '-p',
            help=__("Page number"),
            is_eager=False,
        ),
        statuses: List[SelfHostedStatusEnumDto] = typer.Option(
            ["RUNNING"],
            '--status',
            '-s',
            help=__("Status item (ALL - show all instances)"),
            is_eager=False,
        ),
        no_dialog: Optional[bool] = typer.Option(
            None,
            "--no-dialog",
            "-nd",
            help=__("Start process with default values, without future dialog"),
            is_eager=False,
        ),
):
    """
        List self hosted instances
    """
    path = get_current_directory()
    config, facade = base_global_check_validation(path=path, no_dialog=no_dialog)

    headers = [
        # '#',
        # 'ID',
        'STATUS',
        'TITLE',
        'UNIQUE ID',
        'CPU TYPE',
        'CPU CORES',
        'GPU TYPE',
        'IP ADDRESS',
        'CREATED AT',
        'UPDATED AT'
    ]

    instance_service: InstanceService = facade.get_instance_service()

    typer.echo(__(
        "Start show self-hosted list with statuses: %statuses% (You can show all statuses set up status=ALL)",
        placeholders={
            'statuses': ', '.join([item.value for item in statuses])
        }))

    if SelfHostedStatusEnumDto.find_special_status(statuses=statuses):
        statuses = []

    instance_service.print(
        func_get_data=instance_service.get_self_hosted_list,
        func_special_params={
            'statuses': statuses,
        },
        mapper=SelfHostedMapper(),
        config=config,
        headers=headers,
        row=row,
        page=page,
        no_dialog=no_dialog,
        show_index="never",
    )

    typer.echo(__("List self-hosted done"))
    raise typer.Exit(0)
