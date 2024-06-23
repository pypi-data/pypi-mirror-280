from http import HTTPStatus

import httpx

from omie_client.accounts_payable import AccountsPayable
from omie_client.exceptions import OmieBlockedError, OmieRateLimitError, OmieRequestError


class OmieClient:
    def __init__(
        self,
        app_key: str,
        app_secret: str,
        api_base_url: str = "https://app.omie.com.br/api",
        default_timeout: int = 5,
    ):
        """Omie's API SDK.

        For complete reference of Omie's API look on https://developer.omie.com.br/service-list/.

        Parameters
        ----------
        app_key : str
            The Omie's App Key.
        app_secret : str
            The Omie's App Secret.
        api_base_url : str
            The API base URL. Default as https://app.omie.com.br/api.
        default_timeout : int
            Default requests timeout in seconds.
        """
        self._app_key = app_key
        self._app_secret = app_secret
        self._client = httpx.Client(base_url=api_base_url, timeout=default_timeout, http2=True)

    def request(self, url: str, data: dict) -> dict:
        """Make a request to Omie API's.

        Parameters
        ----------
        url : str
            A endpoint URL to be merged with the API base URL.
        data : dict
            An arbritary dictionary with the resource params.

        Returns
        -------
        dict
            The Omie's API JSON response as dict.

        Raises
        ------
        OmieBlockedError
            In case of Omie's 403 status code response.

        OmieRequestError
            In case of 4xx and 5xx status code response.
        """
        authenticated_data = {"app_key": self._app_key, "app_secret": self._app_secret, **data}

        try:
            response = self._client.post(url, json=authenticated_data)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            if e.response.status_code == HTTPStatus.FORBIDDEN:
                raise OmieBlockedError

            if e.response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
                raise OmieRateLimitError

            error_data = e.response.json()
            raise OmieRequestError(
                status_code=e.response.status_code,
                code=error_data.get("code", "SOAP-ENV:Unknown-error"),
                message=error_data.get("faultstring", "Unknown error"),
            )

    @property
    def accounts_payable(self) -> AccountsPayable:
        return AccountsPayable(self)
