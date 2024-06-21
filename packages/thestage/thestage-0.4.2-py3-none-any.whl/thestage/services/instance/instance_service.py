from typing import Tuple, List, Optional, Any

from thestage_core.entities.config_entity import ConfigEntity

from thestage.services.clients.thestage_api.dtos.enums.selfhosted_status import SelfHostedStatusEnumDto
from thestage.services.clients.thestage_api.dtos.enums.rented_status import RentedStatusEnumDto
from thestage.services.abstract_service import AbstractService
from thestage.helpers.error_handler import error_handler
from thestage.services.clients.thestage_api.api_client import TheStageApiClient
from thestage.services.config_provider.config_provider import ConfigProvider


class InstanceService(AbstractService):

    __thestage_api_client: TheStageApiClient = None

    def __init__(
            self,
            thestage_api_client: TheStageApiClient,
            config_provider: ConfigProvider,
    ):
        super(InstanceService, self).__init__(
            config_provider=config_provider
        )
        self.__thestage_api_client = thestage_api_client

    @error_handler()
    def get_rented_list(
            self,
            config: ConfigEntity,
            statuses: List[RentedStatusEnumDto],
            row: int = 5,
            page: int = 1,
    ) -> Tuple[List[Any], int]:
        data, total_pages = self.__thestage_api_client.get_rented_instance_list(
            token=config.main.auth_token,
            statuses=statuses,
            page=page,
            limit=row,
        )

        return data, total_pages

    @error_handler()
    def get_self_hosted_list(
            self,
            config: ConfigEntity,
            statuses: List[SelfHostedStatusEnumDto],
            row: int = 5,
            page: int = 1,
    ) -> Tuple[List[Any], int]:
        data, total_pages = self.__thestage_api_client.get_self_hosted_instance_list(
            token=config.main.auth_token,
            statuses=statuses,
            page=page,
            limit=row,
        )
        return data, total_pages
