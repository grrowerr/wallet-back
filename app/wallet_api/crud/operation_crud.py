from uuid import UUID

from app.extensions import db
from app.utils.bases.base_crud import BaseCRUD
from app.wallet_api.services.wallet_service import WalletService
from app.wallet_api.transactions.models.transaction_model import TransactionModel
from app.wallet_api.transactions.schemas.transaction_operation_schema import TransactionOperationSchema
from app.wallet_api.wallet.schemas.wallet_response_schema import WalletResponseSchema


class TransactionCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(database=db, model=TransactionModel)

        self.wallet_service = WalletService()
        self.operation_schema = TransactionOperationSchema()
        self.wallet_response_schema = WalletResponseSchema()

    def create(self, transaction_data: dict, wallet_ref: UUID):
        transaction_data['wallet_ref'] = wallet_ref
        transaction_obj = self.operation_schema.load(transaction_data)

        self.db.session.add(transaction_obj)
        self.db.session.flush()

        wallet_obj = self.wallet_service.operation(transaction_data=transaction_data, wallet_ref=wallet_ref)

        self.db.session.commit()

        response_data = self.wallet_response_schema.dump(wallet_obj)
        return response_data
