import http
import json
import webbrowser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth import exceptions
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from database_mysql_local.generic_crud import GenericCRUD
from logger_local.MetaLogger import MetaLogger
from python_sdk_remote.utilities import our_get_env
from user_external_local.user_externals_local import UserExternalsLocal

from .google_account_local_constants import GoogleAccountLocalConstants

USER_EXTERNAL_SCHEMA_NAME = "user_external"
USER_EXTERNAL_TABLE_NAME = "user_external_table"
USER_EXTERNAL_VIEW_NAME = "user_external_view"
USER_EXTERNAL_DEFAULT_COLUMN_NAME = "user_external_id"

# Static token details
SCOPES = ["https://www.googleapis.com/auth/userinfo.email",
          "https://www.googleapis.com/auth/contacts.readonly",
          "https://www.googleapis.com/auth/contacts",
          "openid"]  # Both scopes must be allowed within the project!


class GoogleAccountLocal(GenericCRUD, metaclass=MetaLogger,
                         object=GoogleAccountLocalConstants.LoggerSetupConstants.GOOGLE_ACCOUNT_LOCAL_CODE_LOGGER_OBJECT):
    def __init__(self, is_test_data: bool = False) -> None:
        GenericCRUD.__init__(self,
                             default_schema_name=USER_EXTERNAL_SCHEMA_NAME,
                             default_table_name=USER_EXTERNAL_TABLE_NAME,
                             default_view_table_name=USER_EXTERNAL_VIEW_NAME,
                             default_column_name=USER_EXTERNAL_DEFAULT_COLUMN_NAME,
                             is_test_data=is_test_data)
        self.user_externals_local = UserExternalsLocal()

        self.service = None
        self.creds = None
        self.email = None
        self.google_client_id = our_get_env("GOOGLE_CLIENT_ID", raise_if_empty=True)
        self.google_client_secret = our_get_env("GOOGLE_CLIENT_SECRET", raise_if_empty=True)
        self.google_port_for_authentication = int(our_get_env("GOOGLE_PORT_FOR_AUTHENTICATION", raise_if_empty=True))
        self.google_redirect_uris = our_get_env("GOOGLE_REDIRECT_URIS", raise_if_empty=True)
        self.google_auth_uri = our_get_env("GOOGLE_AUTH_URI", raise_if_empty=True)
        self.google_token_uri = our_get_env("GOOGLE_TOKEN_URI", raise_if_empty=True)

    def authenticate(self, email: str):
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                # If self.creds is None but you have a refresh token
                select_result_dict = self.select_one_dict_by_where(
                    schema_name="user_external", view_table_name="user_external_view",
                    select_clause_value="refresh_token, access_token",
                    where="username=%s AND is_refresh_token_valid=TRUE AND system_id=%s",
                    params=(email, GoogleAccountLocalConstants.GOOGLE_SYSTEM_ID), order_by="user_external_id DESC")
                refresh_token = select_result_dict.get("refresh_token")
                access_token = select_result_dict.get("access_token")
                if not self.creds and refresh_token:
                    self.creds = Credentials(
                        token=access_token,
                        refresh_token=refresh_token,
                        token_uri=self.google_token_uri,
                        client_id=self.google_client_id,
                        client_secret=self.google_client_secret
                    )
                    try:
                        self.creds.refresh(Request())
                    except exceptions.RefreshError as exception:
                        self.logger.exception("google-contact-local Google Refresh token failed.",
                                              object={"exception": exception})
                        exception_message = str(exception)
                        if ("The credentials do not contain the necessary fields" in exception_message) or \
                           ("The credentials returned by the refresh_handler are already expired" in exception_message):
                            # The refresh token can become an invalid
                            self.update_by_column_and_value(
                                schema_name="user_external", table_name="user_external_table",
                                column_name="refresh_token", column_value=refresh_token,
                                data_dict={"is_refresh_token_valid": False})
                            # "end_timestamp": datetime.now(ZoneInfo("UTC"))})
                            self.__authorize()
                else:
                    self.__authorize()

            # Fetch the user's email for profile_id in our DB
            # TODO Can we wrap all indirect calls with Api Management?
            self.service = build('oauth2', 'v2', credentials=self.creds)
            user_info = self.service.userinfo().get().execute()
            self.email = user_info.get("email")
            # TODO: What else can we get from user_info? Please add a link to the documentation and let's have brainstorming

            # Deserialize the token_data into a Python dictionary
            token_data_dict = json.loads(self.creds.to_json())
            # TODO: The following log is throwing an exception, fix it
            # logger.info("GoogleContact.authenticate", {'token_data_dict': token_data_dict})
            # TODO: What other data can we get from token_data_dict?

            # Extract the access_token, expires_in, and refresh_token to insert into our DB
            access_token = token_data_dict.get("token", None)
            expires_in = token_data_dict.get("expiry", None)
            refresh_token = token_data_dict.get("refresh_token", None)

            if access_token:
                self.user_externals_local.insert_or_update_user_external_access_token(
                    system_id=GoogleAccountLocalConstants.GOOGLE_SYSTEM_ID,
                    username=self.email,
                    # We can't get profile_id by email for play1@circ.zone because it's not in profile_view,
                    # this method will always select from view
                    profile_id=self.user_context.get_effective_profile_id(),
                    access_token=access_token,
                    expiry=expires_in,
                    refresh_token=refresh_token)
                # TODO Error handling of the above call
            else:
                raise Exception("Access token not found in token_data.")

    # TODO Please move this method to google-account authenticate repo as it is relevant also to Google Calendar
    def __authorize(self):
        client_config = {
            "installed": {
                "client_id": self.google_client_id,
                "client_secret": self.google_client_secret,
                "redirect_uris": self.google_redirect_uris,
                "auth_uri": self.google_auth_uri,
                "token_uri": self.google_token_uri,
            }
        }
        flow = InstalledAppFlow.from_client_config(client_config, SCOPES, redirect_uri=self.google_redirect_uris)
        auth_url, _ = flow.authorization_url(access_type='offline', prompt='consent')
        # old: self.creds = flow.run_local_server(port=0)
        # if GOOGLE_REDIRECT_URIS is localhost it must be
        # GOOGLE_REDIRECT_URIS=http://localhost:54415/
        # if the port number is 54415 and we must also pass that port
        # to the run_local_server function
        # and also add EXACTLY http://localhost:54415/
        # to Authorised redirect URIs in the
        # OAuth 2.0 Client IDs in Google Cloud Platform

        print(f'Please go to this URL and authorize the application: {auth_url}')
        webbrowser.open(auth_url)

        # If the url is
        # http://localhost:54219/?state=yp8FP2BF7cI9xExjUB70Oyaol0oDNG&code=4/0AdLIrYclkHjKFCb_yJn625Htr8FejaRjFawe7mldEqWINitBz6VD_E0ZOWx0K5d4eocYZg&scope=email%20openid%20https://www.googleapis.com/auth/contacts.readonly%20https://www.googleapis.com/auth/userinfo.email&authuser=0&prompt=consent
        # the auth_code is 4/0AdLIrYclkHjKFCb_yJn625Htr8FejaRjFawe7mldEqWINitBz6VD_E0ZOWx0K5d4eocYZg
        # is found after the code= in the url

        auth_code = input('Enter the authorization code: ')
        flow.fetch_token(code=auth_code)
        self.creds = flow.credentials
        # self.creds = flow.run_local_server(port=self.port)
