from getpass import getpass
from logging import DEBUG
from pathlib import Path
from time import time
from typing import Optional, Type, TypeVar, Union
from urllib.parse import urljoin
from webbrowser import open_new_tab

from jwt import decode as jwt_decode
from pydantic import (
    Field,
    HttpUrl,
    SecretStr,
    ValidationInfo,
    field_serializer,
    field_validator,
)
from pydantic_core import Url
from pydantic_settings import BaseSettings, SettingsConfigDict

from galileo_core.constants.request_method import RequestMethod
from galileo_core.constants.routes import Routes
from galileo_core.helpers.api_client import ApiClient
from galileo_core.helpers.execution import async_run
from galileo_core.helpers.logger import logger

AGalileoConfig = TypeVar("AGalileoConfig", bound="GalileoConfig")


class GalileoConfig(BaseSettings):
    # Debug mode.
    debug: bool = False

    console_url: HttpUrl
    api_url: Optional[HttpUrl] = None

    # User auth details.
    username: Optional[str] = None
    password: Optional[SecretStr] = None
    api_key: Optional[SecretStr] = None
    jwt_token: Optional[SecretStr] = None
    current_user: Optional[str] = None

    # Validated API client. This is set as a part of the initialization.
    # We set the API URL and JWT token on the API client and make a request to
    # confirm that the user is logged in successfully.
    # This is set as an exclude field to avoid serializing it to the config file.
    validated_api_client: Optional[ApiClient] = Field(
        default=None,
        validate_default=True,
        exclude=True,
        description="Validated API client that is with the user's JWT token after a successful login.",
    )

    # Config file for this project.
    config_filename: str = "core-config.json"

    model_config = SettingsConfigDict(
        # Allow loading from environment variables.
        env_prefix="GALILEO_",
        # Allow unknown fields when loading from a config file.
        extra="allow",
    )

    @property
    def config_file(self) -> Path:
        return Path().home().joinpath(".galileo", self.config_filename)

    @field_validator("debug", mode="before")
    def set_debug_mode(cls, value: bool) -> bool:
        """
        If debug is enabled, set the logger to debug mode by adding a stream handler to stderr with a custom formatter.

        Parameters
        ----------
        value : bool
            Value of the debug field.

        Returns
        -------
        bool
            Value of the debug field.
        """
        # if not value:
        # logger.disable("galileo_core")

        if value:
            logger.setLevel(DEBUG)
        return value

    @field_validator("console_url", mode="before")
    def ensure_https_console_url(cls, value: str) -> str:
        """
        Ensure that the console URL is an HTTPS URL.

        Parameters
        ----------
        value : str
            Console URL to validate.

        Returns
        -------
        str
            Validated console URL.
        """
        if value and not (value.startswith("https") or value.startswith("http")):
            value = f"https://{value}"
        return value

    @field_validator("api_url", mode="before")
    def set_api_url(cls, api_url: Optional[Union[str, Url]], info: ValidationInfo) -> Url:
        """
        Set the API URL if it's not already set.

        We can set the API URL in the following ways:
        1. If the API URL is provided, use it.
        2. If the console URL matches `localhost` or `127.0.0.1`, use `http://localhost:8088`.
        3. If the API URL is not provided, use the console URL to generate the API URL
        by replacing `console` with `api`.

        Once we determine the API URL, we make a request to the healthcheck endpoint to
        validate that it is reachable.

        Parameters
        ----------
        api_url : Optional[Union[str, Url]]
            API URL to use. If not provided, we generate it from the console URL.
        info : ValidationInfo
            Pydantic validation info object.

        Returns
        -------
        Url
            API URL to use.

        Raises
        ------
        ValueError
            If the console URL is not set.
        ValueError
            If the API URL can't be generated.
        """
        if api_url is None:
            console_url = info.data.get("console_url")
            if console_url is None:
                raise ValueError(
                    "Console URL is required. Please set the environment variable "
                    "`GALILEO_CONSOLE_URL` to your Galileo console URL."
                )
            else:
                console_url = console_url.unicode_string() if isinstance(console_url, Url) else console_url
            # Local dev.
            if any(["localhost" in console_url, "127.0.0.1" in console_url]):
                api_url = "http://localhost:8088"
            else:
                api_url = console_url.replace("console", "api")
        if api_url is None:
            raise ValueError("API URL is required.")
        else:
            async_run(ApiClient.make_request(RequestMethod.GET, base_url=str(api_url), endpoint=Routes.healthcheck))
        return Url(api_url) if isinstance(api_url, str) else api_url

    @staticmethod
    def get_token_from_ui(console_url: Url) -> str:
        """
        Given a console URL, open the token generation page in the browser and prompt the user to enter the token
        generated.

        Parameters
        ----------
        console_url : Url
            Console URL to use.

        Returns
        -------
        str
            JWT token generated by the user.
        """
        token_url = urljoin(console_url.unicode_string(), Routes.get_token)
        logger.info(f"🔐 Opening {token_url} to generate a new token.")
        try:
            open_new_tab(token_url)
        except Exception:
            # If we can't open the browser, that's fine.
            pass
        finally:
            print(f"Go to {token_url} to generate a new token.")
            return getpass("🔐 Enter your token:")

    @staticmethod
    def get_jwt_token(
        console_url: Optional[Url] = None,
        api_url: Optional[Url] = None,
        api_key: Optional[SecretStr] = None,
        username: Optional[str] = None,
        password: Optional[SecretStr] = None,
    ) -> SecretStr:
        """
        Get the JWT token for the user.

        1. If an API key is provided, log in with the API key.
        2. If a username and password are provided, log in with the username and password.
        3. If no credentials are provided, attempt to log in with a token from the UI.

        Parameters
        ----------
        console_url : Optional[Url], optional
            Console URL, by default None
        api_url : Optional[Url], optional
            API URL, by default None
        api_key : Optional[SecretStr], optional
            API key, by default None
        username : Optional[str], optional
            Username, by default None
        password : Optional[SecretStr], optional
            Password, by default None

        Returns
        -------
        SecretStr
            JWT token for the user, if successful, as a secret string.

        Raises
        ------
        AssertionError
            If the console URL is not provided.
        AssertionError
            If the API URL is not provided.
        """

        token_data = dict()
        assert console_url is not None, "Console URL is required."
        assert api_url is not None, "API URL is required."
        if api_key:
            logger.debug("Logging in with API key.")
            token_data = async_run(
                ApiClient.make_request(
                    RequestMethod.POST,
                    base_url=api_url.unicode_string(),
                    endpoint=Routes.api_key_login,
                    json=dict(api_key=api_key.get_secret_value()),
                )
            )
            logger.debug("Logged in with API key.")
        elif username and password:
            logger.debug("Logging in with username and password.")
            token_data = async_run(
                ApiClient.make_request(
                    RequestMethod.POST,
                    base_url=api_url.unicode_string(),
                    endpoint=Routes.username_login,
                    data=dict(username=username, password=password.get_secret_value(), auth_method="email"),
                )
            )
            logger.debug("Logged in with username and password.")
        if (jwt_token := token_data.get("access_token")) is None:
            logger.debug("No credentials found. Attempting to log in with token.")

            jwt_token = GalileoConfig.get_token_from_ui(console_url)
            logger.debug("Logged in with access token from UI.")
        logger.debug("JWT token received and set.")
        return SecretStr(jwt_token)

    @field_validator("jwt_token", mode="before")
    def set_jwt_token(cls, value: Optional[Union[str, SecretStr]], info: ValidationInfo) -> SecretStr:
        """
        Set the JWT token for the user.

        Parameters
        ----------
        value : Optional[str]
            JWT token to set for the user.
        info : ValidationInfo
            Pydantic validation info object.

        Returns
        -------
        SecretStr
            JWT token as a secret string.
        """
        if value is None:
            console_url, api_url, api_key, username, password = (
                info.data.get("console_url"),
                info.data.get("api_url"),
                info.data.get("api_key"),
                info.data.get("username"),
                info.data.get("password"),
            )
            value = cls.get_jwt_token(console_url, api_url, api_key, username, password)
        assert value is not None, "JWT token is required."
        return SecretStr(value) if isinstance(value, str) else value

    @field_validator("validated_api_client", mode="before")
    def set_validated_api_client(cls, validated_api_client: Optional[ApiClient], info: ValidationInfo) -> ApiClient:
        """
        Set the validated API client.

        This method sets an API client with the validated API URL and JWT token. As a
        part of the validation process, we make a request to get the current user's email
        address to confirm that the user is logged in successfully.

        Parameters
        ----------
        validated_api_client : Optional[ApiClient]
            API client to set.
        info : ValidationInfo
            Pydantic validation info object.

        Returns
        -------
        ApiClient
            Validated API client.
        """
        console_url, api_url, jwt_token = (
            info.data.get("console_url"),
            info.data.get("api_url"),
            info.data.get("jwt_token"),
        )
        assert api_url is not None, "API URL is required."
        assert jwt_token is not None, "JWT token is required."
        validated_api_client = ApiClient(host=api_url, jwt_token=jwt_token)
        # Get the current user to confirm that the user is logged in successfully.
        current_user = validated_api_client.request(RequestMethod.GET, path=Routes.current_user).get("email")
        logger.debug("Logged in successfully.")
        print(f"👋 You have logged into 🔭 Galileo ({console_url}) as {current_user}.")
        return validated_api_client

    @field_serializer("password", "jwt_token", "api_key", when_used="json-unless-none")
    def serialize_secrets(self, value: SecretStr) -> str:
        """Serialize secret strings to their secret values."""
        return value.get_secret_value()

    def write(self) -> None:
        """
        Write the config object to a file.

        This is only used as a backup for debugging and never read from to set current values.
        """
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        self.config_file.write_text(self.model_dump_json(exclude_none=True))

    def refresh_jwt_token(self) -> None:
        """Refresh token if not present or expired."""
        # Check to see if our token is expired before making a request and refresh token if it's expired.
        if self.jwt_token:
            claims = jwt_decode(self.jwt_token.get_secret_value(), options={"verify_signature": False})
            if claims.get("exp", 0) < time():
                logger.debug("JWT token is invalid, refreshing.")
                self.jwt_token = self.get_jwt_token(
                    self.console_url, self.api_url, self.api_key, self.username, self.password
                )
            else:
                logger.debug("JWT token is still valid, not refreshing.")
        # If no token is present, log in.
        else:
            logger.debug("JWT token not found, getting a new one.")
            self.jwt_token = self.get_jwt_token(
                self.console_url, self.api_url, self.api_key, self.username, self.password
            )

    @property
    def api_client(self) -> ApiClient:
        """
        Get the API client.

        We refresh the JWT token if it's expired and set the JWT token on the API client
        if it's different from the one set on the API client during the config
        initialization.

        Returns
        -------
        ApiClient
            Validated API client.
        """
        assert self.validated_api_client is not None, "API client must be set before accessing it."
        self.refresh_jwt_token()
        if self.jwt_token and self.validated_api_client.jwt_token != self.jwt_token:
            self.validated_api_client.jwt_token = self.jwt_token
        return self.validated_api_client

    @classmethod
    def get(cls: Type[AGalileoConfig]) -> "AGalileoConfig":
        """
        If a config file exists, load it and return the config object. Otherwise, return a new config object.

        If the console URL has changed, return a new config object instead.
        """
        global _config
        if _config is None:
            _config = cls()
            logger.debug("Config set from environment variables.")
            assert _config is not None, "Config object must be set."
            _config.write()
        # Ignore the type here because we know that _config is not None and is an object of
        # the GalileoConfig class or its sub-classes.
        return _config  # type: ignore[return-value]

    def reset(self) -> None:
        """
        Reset the credentials stored in the config object.

        Sub-classes can extend this method to reset additional fields.
        """
        self.username = None
        self.password = None
        self.api_key = None
        self.jwt_token = None
        self.current_user = None
        self.validated_api_client = None
        self.write()

    def logout(self) -> None:
        """Logout the user by resetting the credentials and printing a message."""
        self.reset()
        print(f"👋 You have logged out of 🔭 Galileo ({self.console_url}).")


# Global config object that is used to store the config object after the first load.
_config: Optional[GalileoConfig] = None
