from marshmallow import fields, Schema

from app.utils.enums import TransactionTypeEnum


class DepositSchema(Schema):
    wallet_ref = fields.UUID(
        required=True,
        allow_none=False
    )
    amount = fields.Decimal(
        required=True,
        allow_none=False
    )
    type = fields.Enum(
        enum=TransactionTypeEnum,
        required=True,
        allow_none=False
    )
    description = fields.String(
        required=False,
        allow_none=True
    )
