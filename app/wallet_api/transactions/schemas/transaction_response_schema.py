from marshmallow import Schema

from app.wallet_api.transactions.models.transaction_model import TransactionModel


class TransactionResponseSchema(Schema):
    class Meta:
        model = TransactionModel
        ordered = True
        dump_only = ('ref', 'wallet_ref', 'amount', 'type', 'status', 'description', 'created_at')
        include_fk = True
        load_instance = False
        include_relationships = False
