import typing

if typing.TYPE_CHECKING:
    from omie_client.client import OmieClient


class Endpoint:
    def __init__(self, omie_client: "OmieClient") -> None:
        self._omie_client = omie_client
