from typing import Optional, Dict, Tuple

from thestage_core.entities.config_entity import ConfigEntity

from thestage.i18n.translation import __
from thestage.helpers.logger.app_logger import app_logger
from thestage.services.config_provider.config_provider import ConfigProvider
from thestage.services.service_facade import ServiceFacade
from thestage.controllers.utils_controller import base_check_validation, get_current_directory
from thestage import __app_name__, __version__

import typer

app = typer.Typer(no_args_is_help=True)


@app.command(no_args_is_help=False)
def version():
    """
        return Name and Version app
    """
    path = get_current_directory()
    app_logger.info(f'Start version from {path}')
    typer.echo(
        __("%app_name% v%version%", {'app_name': __app_name__, 'version': __version__}))
    raise typer.Exit(0)


@app.command(name='config', no_args_is_help=True, help=__("Help change some config items"))
def config(
        working_directory: Optional[str] = typer.Option(
            None,
            "--working-directory",
            "-wd",
            help=__("Full path for working directory"),
            is_eager=False,
        ),
        change_token: bool = typer.Option(
            False,
            "--change-token",
            "-ct",
            help=__("If you want initialize change token"),
            is_eager=False,
            is_flag=True,
        ),
        clear_env: bool = typer.Option(
            False,
            "--clear-env",
            "-cenv",
            help=__("Help clear env, after update command cli"),
            is_eager=False,
            is_flag=True,
        ),
):
    """
        Help update
    """
    path = get_current_directory()
    app_logger.info(f'Start config from {path}')

    config_provider = ConfigProvider(
        project_path=path if not working_directory else working_directory,
        only_global=True,
    )
    facade = ServiceFacade(config_provider=config_provider)
    config: ConfigEntity = config_provider.get_full_config(only_global=True)
    app_service = facade.get_app_config_service()

    if change_token:
        app_service.app_change_token(config=config, only_global=True)

    if clear_env:
        app_service.app_remove_env()

    raise typer.Exit(0)
