from typing import Dict, Any

from marshmallow import Schema, post_load, fields, RAISE

from app.utils.enums import CurrencyEnum
from app.wallet_api.wallet.models.wallet_model import WalletModel


class WalletCreateSchema(Schema):
    """
    Схема для валидации данных Wallet.
    """
    class Meta:
        ordered = True
        unknown = RAISE

    currency = fields.Enum(
        enum=CurrencyEnum,
        required=True,
        allow_none=False
    )

    # noinspection unused-parameter
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
