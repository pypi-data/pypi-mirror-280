import requests
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.MetaLogger import MetaLogger
from python_sdk_remote.http_response import create_authorization_http_headers
from python_sdk_remote.utilities import get_brand_name, get_environment_name
from url_remote.action_name_enum import ActionName
from url_remote.component_name_enum import ComponentName
from url_remote.entity_name_enum import EntityName
from url_remote.our_url import OurUrl
from user_context_remote.user_context import UserContext

SMARTLINK_COMPONENT_ID = 258
SMARTLINK_COMPONENT_NAME = "smart link remote"
DEVELOPER_EMAIL = "akiva.s@circ.zone"
logger_object = {
    'component_id': SMARTLINK_COMPONENT_ID,
    'component_name': SMARTLINK_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}

SMARTLINK_REMOTE_API_VERSION = 1


class SmartlinkRemote(metaclass=MetaLogger, object=logger_object):
    def __init__(self, is_test_data: bool = False) -> None:
        self.user_context = UserContext()
        self.is_test_data = is_test_data

    def get_smartlink(self, identifier: str) -> requests.Response:
        """response.json() fields:
        statusCode, body
        inside body: message, input, smartlink_details (or error & traceback)
        """
        url = self.get_smartlink_url(
            smartlink_action=ActionName.GET_SMARTLINK_DATA_BY_IDENTIFIER,
            identifier=identifier)
        response = self._call_response_by_action_name(url=url)
        return response

    def execute_smartlink(self, identifier: str) -> requests.Response:
        """response.json() fields:
        statusCode, body
        inside body: message, input (+ error & traceback if error)
        """
        url = self.get_smartlink_url(
            smartlink_action=ActionName.EXECUTE_SMARTLINK_BY_IDENTIFIER,
            identifier=identifier)
        response = self._call_response_by_action_name(url=url)
        return response

    @staticmethod
    def get_smartlink_url(*, identifier: str,
                          smartlink_action: ActionName = ActionName.EXECUTE_SMARTLINK_BY_IDENTIFIER) -> str:
        path_parameters = {"identifier": identifier}
        # https://vtwvknaf08.execute-api.us-east-1.amazonaws.com/dev/play1/api/v1/smartlink/{smartlink_action}/{identifier}
        # smartlink_action = getSmartlinkDataByIdentifier OR executeSmartlinkByIdentifier
        url = OurUrl.endpoint_url(
            brand_name=get_brand_name(),
            environment_name=get_environment_name(),
            component_name=ComponentName.SMARTLINK.value,
            entity_name=EntityName.SMARTLINK.value,
            version=SMARTLINK_REMOTE_API_VERSION,
            action_name=smartlink_action.value,
            path_parameters=path_parameters
        )
        return url

    def _call_response_by_action_name(self, url: str) -> requests.Response:
        user_jwt = self.user_context.get_user_jwt()
        header = create_authorization_http_headers(user_jwt)
        payload = {"isTestData": self.is_test_data}
        response = requests.get(url, json=payload, headers=header)
        return response
