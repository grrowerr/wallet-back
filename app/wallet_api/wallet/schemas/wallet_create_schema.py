import uuid
from typing import Dict, Any

from marshmallow_sql import Schema, post_load, fields, RAISE

from app.wallet_api.wallet.models.wallet_model import WalletModel


class WalletCreateSchema(Schema):
    """
    Схема для валидации данных Wallet.
    """
    class Meta:
        unknown = RAISE

    ref = fields.UUID(
        required=False,
        dump_only=True,

    )


    @post_load
    def make_wallet(
            self,
            wallet_data: Dict[str, Any],
            **kwargs
    ) -> WalletModel:
        """
        Создание объекта модели.
        Args:
            wallet_data (Dict[str, Any]): Данные для создания объекта.
        Returns:
            WalletModel: Созданный объект.
        """

        new_wallet = WalletModel(**wallet_data)
        return new_wallet
