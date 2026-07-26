from uuid import UUID

from app.extensions import db
from app.utils.enums import TransactionTypeEnum
from app.wallet_api.wallet.models.wallet_model import WalletModel


class WalletService:

    @staticmethod
    def operation(transaction_data: dict, wallet_ref: UUID) -> WalletModel:
        operation_type = transaction_data['type']
        amount = transaction_data['amount']
        wallet = db.session.query(WalletModel).get(wallet_ref)

        if operation_type == TransactionTypeEnum.DEPOSIT.value:
            wallet.balance += amount
        elif operation_type == TransactionTypeEnum.WITHDRAW.value:
            if wallet.balance < amount:
                raise ValueError('На балансе кошелька не хватает средств!')
            wallet.balance -= amount
        else:
            raise TypeError('Тип транзакции не поддерживается!')
        db.session.add(wallet)
        db.session.flush()

        return wallet
    