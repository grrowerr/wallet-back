from typing import Dict, Any

from marshmallow import fields, Schema, post_load

from app.utils.enums import TransactionTypeEnum
from app.wallet_api.transactions.models.transaction_model import TransactionModel


class TransactionOperationSchema(Schema):
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

    # noinspection unused-parameter
    @post_load
    def create_transaction_obj(
            self,
            transaction_data: Dict[str, Any],
            **kwargs

    ) -> TransactionModel:

        """
        Создание объекта модели.

        :param transaction_data: Данные для создания объекта.
        :returns: TransactionModel
        """

        new_transaction = TransactionModel(**transaction_data)
        return new_transaction
