from typing import Union, overload
from typing_extensions import Self
from .openai import ScalifyClient, AsyncScalifyClient
from openai import Client, AsyncClient


class Scalify:
    @overload
    def __new__(cls: type[Self], client: "Client") -> "ScalifyClient":
        ...

    @overload
    def __new__(cls: type[Self], client: "AsyncClient") -> "AsyncScalifyClient":
        ...

    def __new__(
        cls: type[Self], client: Union["Client", "AsyncClient"]
    ) -> Union["ScalifyClient", "AsyncScalifyClient"]:
        if isinstance(client, AsyncClient):
            return AsyncScalifyClient(client=client)
        return ScalifyClient(client=client)

    @classmethod
    def wrap(
        cls: type[Self], client: Union["Client", "AsyncClient"]
    ) -> Union["Client", "AsyncClient"]:
        if isinstance(client, AsyncClient):
            return AsyncScalifyClient.wrap(client=client)
        return ScalifyClient.wrap(client=client)
