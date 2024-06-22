import json
from http import HTTPStatus
from functools import lru_cache

import requests
from language_remote.lang_code import LangCode
from python_sdk_remote.mini_logger import MiniLogger as logger
from python_sdk_remote.utilities import get_brand_name, get_environment_name, our_get_env
from python_sdk_remote.http_response import create_return_http_headers
from url_remote import action_name_enum, component_name_enum, entity_name_enum
from url_remote.our_url import OurUrl

# TODO Shall we use authentication-remote-python-package and not directly authentication-local-restapi-typescript?

BRAND_NAME = get_brand_name()
ENVIORNMENT_NAME = get_environment_name()

# TODO How about using AUTHENTICATION_API_VERSION_DICT per environment_name in url-remote-python-package?
# TODO This should be array in url-remote, right? Please change all of the API_VERSIONs to array
AUTHENTICATION_API_VERSION = 1
DEFAULT_LANG_CODE = LangCode.ENGLISH

# TODO: use data class instead of getter & setters
class UserContext:
    @lru_cache  # instance per unique combination of user_identifier, password, user_jwt
    def __new__(cls, user_identifier: str = None, password: str = None, user_jwt: str = None):
        user = super(UserContext, cls).__new__(cls)
        user._initialize(user_identifier=user_identifier, password=password, user_jwt=user_jwt)
        return user

    def _initialize(self, user_identifier: str = None, password: str = None, user_jwt: str = None) -> None:
        # self.user_identifier = user_identifier
        # self.password = password
        self.user_jwt = user_jwt
        self.real_user_id = None
        self.real_profile_id = None
        self.effective_user_id = None
        self.effective_profile_id = None
        self.lang_code_str: str or None = None
        self.real_first_name = None
        self.real_last_name = None
        self.real_display_name = None
        self.subscription_id = 5  # TODO temp solution, so we can debug
        if user_jwt:
            # TODO validate_user_jwt_response -> authenticate_product_user_response (as it is not always user_jwt)
            validate_user_jwt_response = self._authenticate_by_user_jwt(user_jwt=user_jwt)
        else:
            user_identifier = user_identifier or our_get_env("PRODUCT_USER_IDENTIFIER")
            password = password or our_get_env("PRODUCT_PASSWORD")
            validate_user_jwt_response = self._authenticate_by_user_identification_and_password(
                user_identifier=user_identifier, password=password)
        # Populate the private data members with data we received from Authentication Local REST-API https://github.com/circles-zone/authentication-local-restapi-typescript-serverless-com/edit/dev/auth-restapi-serverless-com/src/services/auth-service/auth-service-impl.ts
        self.__get_user_data_login_response(validate_user_jwt_response=validate_user_jwt_response)

    @staticmethod
    @lru_cache
    def login_using_user_identification_and_password(user_identifier: str = None, password: str = None):
        # LOGIN_USING_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME = "login_using_user_identification_and_password"
        # TODO Why commented? Shall we add if (DebugMode)
        # logger.start(LOGIN_USING_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME, object={"user_identifier": user_identifier, "password": password})
        if user_identifier is None:
            user_identifier = our_get_env("PRODUCT_USER_IDENTIFIER")
        if password is None:
            password = our_get_env("PRODUCT_PASSWORD")
        if not user_identifier or not password:
            # To support cases with no PRODUCT_USER_IDENTIFIER and PRODUCT_PASSWORD in the deployment.
            logger.warning(
                "Warning: missing PRODUCT_USER_IDENTIFIER or PRODUCT_PASSWORD in .env file - WARNING -")
            return None
        user = UserContext(user_identifier=user_identifier, password=password)
        # logger.end(LOGIN_USING_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME,object={"user": str(user)})
        return user

    @staticmethod
    @lru_cache
    def login_using_user_jwt(user_jwt: str) -> 'UserContext':
        # LOGIN_USING_USER_JWT_METHOD_NAME = "login_using_user_jwt"
        # logger.start(LOGIN_USING_USER_JWT_METHOD_NAME ,object={"user_jwt": user_jwt})
        user = UserContext(user_jwt=user_jwt)
        # logger.end(LOGIN_USING_USER_JWT_METHOD_NAME,object={"user": str(user)})
        return user

    def _set_real_user_id(self, user_id: int) -> None:
        #  # SET_REAL_USER_ID_METHOD_NAME = "_set_real_user_id"
        # logger.start(SET_REAL_USER_ID_METHOD_NAME,object={"user_id": user_id})
        self.real_user_id = user_id
        # logger.end(SET_REAL_USER_ID_METHOD_NAME)

    def _set_real_profile_id(self, profile_id: int) -> None:
        # SET_REAL_PROFILE_ID_METHOD_NAME = "_set_real_profile_id"
        # logger.start(SET_REAL_PROFILE_ID_METHOD_NAME,object={"profile_id": profile_id})
        self.real_profile_id = profile_id
        # logger.end(SET_REAL_PROFILE_ID_METHOD_NAME)

    def get_real_user_id(self) -> int:
        # GET_REAL_USER_ID_METHOD_NAME = "get_real_user_id"
        # logger.start(GET_REAL_USER_ID_METHOD_NAME)
        # logger.end(GET_REAL_USER_ID_METHOD_NAME,object={"user_id": self.real_user_id})
        return self.real_user_id

    def get_real_profile_id(self) -> int:
        # GET_REAL_PROFILE_ID_METHOD_NAME = "get_real_profile_id"
        # logger.start(GET_REAL_PROFILE_ID_METHOD_NAME)
        # logger.end(GET_REAL_PROFILE_ID_METHOD_NAME,object={"user_id": self.real_profile_id})
        return self.real_profile_id

    def get_effective_profile_preferred_lang_code_string(self) -> str:
        # GET_CURENT_LANG_CODE_STRING_METHOD_NAME = "get_effective_profile_preferred_lang_code"
        # logger.start(GET_CURENT_LANG_CODE_STRING_METHOD_NAME)
        # logger.end(GET_CURENT_LANG_CODE_STRING_METHOD_NAME,object={"lang_code_string": self.lang_code})
        return self.lang_code_str or DEFAULT_LANG_CODE.value

    def get_effective_profile_preferred_lang_code(self) -> LangCode:
        return LangCode(self.lang_code_str or DEFAULT_LANG_CODE.value)

    def _set_effective_profile_preferred_lang_code(self, lang_code: LangCode) -> None:
        # SET_CURRENT_LANG_CODE_METHOD_NAME = "_set_current_lang_code"
        # logger.start(SET_CURRENT_LANG_CODE_METHOD_NAME,object={"lang_code": lang_code.value})
        self.lang_code_str = lang_code.value
        # logger.end(SET_CURRENT_LANG_CODE_METHOD_NAME)

    def _set_real_first_name(self, first_name: str) -> None:
        # SET_REAL_FIRST_NAME_METHOD_NAME = "_set_real_first_name"
        # logger.start(SET_REAL_FIRST_NAME_METHOD_NAME,object={"first_name": first_name})
        self.real_first_name = first_name
        # logger.end(SET_REAL_FIRST_NAME_METHOD_NAME)

    def _set_real_last_name(self, last_name: str) -> None:
        # SET_REAL_LAST_NAME_METHOD_NAME = "_set_real_last_name"
        # logger.start(SET_REAL_LAST_NAME_METHOD_NAME,object={"first_name": last_name})
        self.real_last_name = last_name
        # logger.end(SET_REAL_LAST_NAME_METHOD_NAME)

    def get_real_first_name(self) -> str:
        # GET_REAL_FIRST_NAME_METHOD_NAME = "get_real_first_name"
        # logger.start(GET_REAL_FIRST_NAME_METHOD_NAME)
        # logger.end(GET_REAL_FIRST_NAME_METHOD_NAME,object={"first_name": self.real_first_name})
        return self.real_first_name

    def get_real_last_name(self) -> str:
        # GET_REAL_LAST_NAME_METHOD_NAME = "get_real_last_name"
        # logger.start(GET_REAL_LAST_NAME_METHOD_NAME)
        # logger.end(GET_REAL_LAST_NAME_METHOD_NAME,object={"last_name": self.real_last_name})
        return self.real_last_name

    def _set_real_name(self, name: str) -> None:
        # SET_REAL_NAME_METHOD_NAME = "_set_real_name"
        # logger.start(SET_REAL_NAME_METHOD_NAME,object={"first_name": name})
        self.real_display_name = name
        # logger.end(SET_REAL_NAME_METHOD_NAME)

    def get_real_name(self) -> str:
        # GET_REAL_NAME_METHOD_NAME = "get_real_name"
        # logger.start(GET_REAL_NAME_METHOD_NAME)
        # logger.end(GET_REAL_NAME_METHOD_NAME,object={"first_name": self.real_first_name})
        return self.real_display_name

    def get_user_jwt(self) -> str:
        return self.user_jwt

    def get_effective_user_id(self) -> int:
        return self.effective_user_id

    def get_effective_profile_id(self) -> int:
        return self.effective_profile_id

    def _set_effective_user_id(self, user_id: int) -> None:
        self.effective_user_id = user_id

    def _set_effective_profile_id(self, profile_id: int) -> None:
        self.effective_profile_id = profile_id

    def _set_effective_subscription_id(self, subscription_id: int) -> None:
        self.subscription_id = subscription_id

    def get_effective_subscription_id(self) -> int:
        # GET_EFFECTIVE_SUBSCRIPTION_ID_METHOD_NAME = "get_effective_subscription_id"
        # logger.warning("user-context-python-package " + GET_EFFECTIVE_SUBSCRIPTION_ID_METHOD_NAME +
        #                " Please make sure get_effective_subscription_id() subscription_id=" + str(
        #     self.subscription_id))
        return self.subscription_id

    def _authenticate_by_user_identification_and_password(
            self, user_identifier: str, password: str) -> requests.Response:
        AUTHENTICATE_BY_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME = "_authenticate_by_user_identification_and_password"
        logger.start(AUTHENTICATE_BY_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME, object={
            "userIdentifier": user_identifier, "password": "***"})
        try:
            authentication_login_enpoint_url = OurUrl.endpoint_url(
                brand_name=BRAND_NAME,
                environment_name=ENVIORNMENT_NAME,
                component_name=component_name_enum.ComponentName.AUTHENTICATION.value,
                entity_name=entity_name_enum.EntityName.AUTH_LOGIN.value,
                version=AUTHENTICATION_API_VERSION,
                action_name=action_name_enum.ActionName.LOGIN.value
            )
            authentication_login_request_dict = {"userIdentifier": user_identifier, "password": password}
            # TOOD Please use get_http_headers() from Python-SDK
            headers = create_return_http_headers()
            authentication_login_response_json = requests.post(
                url=authentication_login_enpoint_url,
                data=json.dumps(authentication_login_request_dict, separators=(",", ":")), headers=headers
            )
            if authentication_login_response_json.status_code != HTTPStatus.OK:
                logger.error(AUTHENTICATE_BY_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME +
                             " authentication_login_response_json.status_code != HTTPStatus.OK " + authentication_login_response_json.text)
                raise Exception(authentication_login_response_json.text)
            # Maybe there is no "data"
            logger.info("authentication_login_response_json.json()" + str(authentication_login_response_json))
            logger.info("authentication_login_response_json.json() with json()" + str(
                authentication_login_response_json.json()))
            self.__process_response(authentication_login_response_json)
            logger.end(AUTHENTICATE_BY_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME, object={
                "user_jwt": self.user_jwt})
            return authentication_login_response_json
        # TODO Catch KeyError: 'data'
        except Exception as exception:
            logger.exception(
                "Error(Exception): user-context-remote-python _authenticate() " + str(exception))
            logger.end(AUTHENTICATE_BY_USER_IDENTIFICATION_AND_PASSWORD_METHOD_NAME)
            raise

    def __process_response(self, authentication_login_response_json):
        try:
            response_json = authentication_login_response_json.json()
            data = response_json.get("data")
            if data is None:
                logger.error("Error: 'data' not found in authentication_login_response_json.json()",
                             object={"authentication_login_response_json": authentication_login_response_json.text,
                                        "response_json": response_json})
            else:
                self.user_jwt = data.get("userJwt")
                if self.user_jwt is None:
                    logger.error(
                        "Error: 'userJwt' not found in 'data'.",
                        object={"data": data,
                                "authentication_login_response_json": authentication_login_response_json.text})
        except Exception as exception:
            logger.error(
                "Error(Exception): user-context-remote-python _authenticate() " + str(exception),
                object={"authentication_login_response_json": authentication_login_response_json.text})

    def _authenticate_by_user_jwt(self, user_jwt: str) -> requests.Response:
        AUTHENTICATE_BY_USER_JWT_METHOD_NAME = "_authenticate_by_user_jwt"
        logger.start(AUTHENTICATE_BY_USER_JWT_METHOD_NAME,
                     object={"user_jwt": user_jwt})
        authentication_login_validate_user_jwt_url = OurUrl.endpoint_url(
            brand_name=BRAND_NAME,
            environment_name=ENVIORNMENT_NAME,
            component_name=component_name_enum.ComponentName.AUTHENTICATION.value,
            entity_name=entity_name_enum.EntityName.AUTH_LOGIN.value,
            # TODO This should be an array per environment in url-remote, right? - Please fix all of them in url-remote to be array.
            version=AUTHENTICATION_API_VERSION,
            action_name=action_name_enum.ActionName.VALIDATE_USER_JWT.value
        )
        validate_user_jwt_request_dict = {"userJwt": user_jwt}
        headers = create_return_http_headers()
        authentication_login_validate_user_jwt_response = requests.post(
            url=authentication_login_validate_user_jwt_url,
            data=json.dumps(validate_user_jwt_request_dict, separators=(",", ":")), headers=headers
        )
        if authentication_login_validate_user_jwt_response.status_code != HTTPStatus.OK:
            logger.error(
                "user-context-remote-python-package _authenticate_by_user_jwt() authentication_login_validate_user_jwt_response.status_code != HTTPStatus.OK " + authentication_login_validate_user_jwt_response.text)
            # MiniLoger.end()
            raise Exception(authentication_login_validate_user_jwt_response.text)
        logger.end(AUTHENTICATE_BY_USER_JWT_METHOD_NAME,
                   object={"validate_user_jwt_response": authentication_login_validate_user_jwt_response})
        return authentication_login_validate_user_jwt_response

    # this private method is being used only in one place
    # TODO validate_user_jwt_response -> authenticate_product_user_response
    def __get_user_data_login_response(self, validate_user_jwt_response: requests.Response) -> None:
        _GET_USER_DATA_LOGIN_RESPONSE_METHOD_NAME = "get_user_data_login_response"
        # validate_user_jwt_response created in Authentication Local REST-API https://github.com/circles-zone/authentication-local-restapi-typescript-serverless-com/edit/dev/auth-restapi-serverless-com/src/services/auth-service/auth-service-impl.ts
        # TODO validate_user_jwt_data_dict
        response_json = validate_user_jwt_response.json()
        data_dict = response_json.get('data')
        first_name = last_name = None
        if not data_dict:
            logger.error(_GET_USER_DATA_LOGIN_RESPONSE_METHOD_NAME + " data from validate_user_jwt_response",
                         object={"validate_user_jwt_response": validate_user_jwt_response.text})
            raise Exception("Can't get data from validate_user_jwt_response: " + validate_user_jwt_response.text)
        if "userDetails" in data_dict:
            # TODO user_details
            user_details: dict = data_dict.get("userDetails")

            if "profileId" in user_details:
                profile_id = user_details.get("profileId")
                self._set_real_profile_id(int(profile_id))
                self._set_effective_profile_id(int(profile_id))

            if "userId" in user_details:
                user_id = user_details.get("userId")
                self._set_effective_user_id(int(user_id))
                self._set_real_user_id(int(user_id))

            if "profilePreferredLangCode" in user_details:
                lang_code = user_details.get("profilePreferredLangCode")
                if lang_code is None:  # default lang_code is en
                    lang_code = "en"
                # change to lang_code enum object
                lang_code = LangCode(lang_code)
                self._set_effective_profile_preferred_lang_code(lang_code)

            if "firstName" in user_details:
                first_name = user_details.get("firstName")
                self._set_real_first_name(first_name)

            if "lastName" in user_details:
                last_name = user_details.get("lastName")
                self._set_real_last_name(last_name)

            if "subscriptionId" in user_details:
                subscription_id = user_details.get("subscriptionId")
                logger.end(
                    _GET_USER_DATA_LOGIN_RESPONSE_METHOD_NAME + " Got subscription_id from the cloud. subscription_id=" +
                    str(subscription_id), object={"subscription_id": subscription_id})
                self._set_effective_subscription_id(subscription_id)

            if self.real_first_name is not None and self.real_last_name is not None:
                name = first_name + " " + last_name
            else:
                # If first_name and last_name are not available, use the email as the name
                name = user_details.get("email")

            self._set_real_name(name)

    def get_country_code(self) -> int:  # TODO: temp solution
        return 972

# from #logger_local.#loggerComponentEnum import #loggerComponentEnum
# from #logger_local.#logger import #logger

# USER_CONTEXT_LOCAL_PYTHON_COMPONENT_ID = 197
# USER_CONTEXT_LOCAL_PYTHON_COMPONENT_NAME = "User Context python package"
# DEVELOPER_EMAIL = "idan.a@circ.zone"
# obj = {
#     'component_id': USER_CONTEXT_LOCAL_PYTHON_COMPONENT_ID,
#     'component_name': USER_CONTEXT_LOCAL_PYTHON_COMPONENT_NAME,
#     'component_category': #loggerComponentEnum.ComponentCategory.Code.value,
#     'developer_email': DEVELOPER_EMAIL
# }
# #logger = #logger.create_#logger(object=obj)

# Commented as we get the decoded user_user_jwt from the authentication service and the user-context do not have access to the USER_JWT_SECRET_KEY
# def get_user_json_by_user_user_jwt(self, user_jwt: str) -> None:
#     if user_jwt is None or user_jwt == "":
#         raise Exception(
#             "Your .env PRODUCT_NAME or PRODUCT_PASSWORD is wrong")
#     #logger.start(object={"user_jwt": user_jwt})
#     try:
#         secret_key = our_get_env("JWT_SECRET_KEY")
#         if secret_key is not None:
#             decoded_payload = jwt.decode(user_jwt, secret_key, algorithms=[
#                                          "HS256"], options={"verify_signature": False})
#             self.profile_id = int(decoded_payload.get('profileId'))
#             self.user_id = int(decoded_payload.get('userId'))
#             self.profilePreferredLangCode = decoded_payload.get('profilePreferredLangCode')
#             #logger.end()
#     except jwt.ExpiredSignatureError as e:
#         # Handle token expiration
#         #logger.exception(object=e)
#         print("Error: userJwt has expired.", sys.stderr)
#         #logger.end()
#         raise
#     except jwt.InvalidTokenError as e:
#         # Handle invalid token
#         #logger.exception(object=e)
#         print("Error:Invalid userJwt.", sys.stderr)
#         #logger.end()
#         raise
