from uuid import UUID

from app.extensions import db
from app.utils.bases.base_crud import BaseCRUD
from app.wallet_api.wallet.models.wallet_model import WalletModel


class WalletCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(database=db, model=WalletModel)

    def read_balance(self, wallet_ref: UUID):
        """
        Возвращает баланс кошелька, по запрашиваемому ref.

        :param wallet_ref: (UUID) Уникальный идентификатор кошелька, баланс которого  возвращаем
        """

        wallet_obj = self.get_by_ref(ref=wallet_ref)

        balance = wallet_obj.balance

        return balance
