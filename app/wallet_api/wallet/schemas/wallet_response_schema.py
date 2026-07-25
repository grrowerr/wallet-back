from marshmallow import fields

from app.utils.bases.base_schema import BaseSchema
from app.utils.enums import CurrencyEnum


class WalletResponseSchema(BaseSchema):
    """
    Схема для отправки данных Wallet.
    """

    balance = fields.Decimal(
        required=True,
        as_string=True,
        places=2
    )
    currency = fields.Enum(
        enum=CurrencyEnum,
        required=True,
        allow_none=False
    )
