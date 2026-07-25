from marshmallow import fields

from app.wallet_api.wallet.schemas.wallet_response_schema import WalletResponseSchema


class WalletWithTransactionsSchema(WalletResponseSchema):
    """
    Схема для отправки данных Wallet со списком транзакций.
    """

    transactions = fields.Nested(
        'TransactionResponseSchema',
        many=True
    )
