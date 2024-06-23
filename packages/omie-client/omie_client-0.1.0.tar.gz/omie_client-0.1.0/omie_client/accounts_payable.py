import typing
from datetime import date, datetime
from decimal import Decimal

from pydantic import StringConstraints, field_validator
from pydantic.dataclasses import dataclass
from typing_extensions import Annotated

from omie_client.endpoint import Endpoint

StrictStr = Annotated[str, StringConstraints(strip_whitespace=True)]


@dataclass(frozen=True)
class Payment:
    codigo_lancamento_omie: int
    codigo_lancamento_integracao: StrictStr
    codigo_cliente_fornecedor: int
    codigo_cliente_fornecedor_integracao: StrictStr
    data_vencimento: date
    valor_documento: Decimal
    codigo_categoria: StrictStr
    data_previsao: date
    id_conta_corrente: int
    observacao: StrictStr
    valor_pis: Decimal
    retem_pis: bool
    valor_cofins: Decimal
    retem_cofins: bool
    valor_csll: Decimal
    retem_csll: bool
    valor_ir: Decimal
    retem_ir: bool
    valor_iss: Decimal
    retem_iss: bool
    numero_pedido: StrictStr
    status_titulo: StrictStr
    codigo_barras_ficha_compensacao: StrictStr

    @field_validator("data_vencimento", "data_previsao", mode="before")
    @classmethod
    def parse_date(cls, value: str) -> date:
        return datetime.strptime(value, "%d/%m/%Y").date()

    @field_validator("retem_pis", "retem_cofins", "retem_csll", "retem_ir", "retem_iss", mode="before")
    @classmethod
    def parse_string_boolean(cls, value: str) -> str:
        return value == "S"


class AccountsPayable(Endpoint):
    ENDPOINT_URL: typing.ClassVar[str] = "/v1/financas/contapagar/"

    def get_by_id(self, omie_id: int) -> Payment:
        """Get a payment by its Omie's ID.

        Parameters
        ----------
        omie_id : int
            The payment Omie's ID.

        Returns
        -------
        Payment
        """
        response = self._omie_client.request(
            self.ENDPOINT_URL,
            data={"call": "ConsultarContaPagar", "param": [{"codigo_lancamento_omie": omie_id}]},
        )

        return Payment(**response)
