import datetime
import uuid

from sqlalchemy.dialects.postgresql.base import UUID

from app.extensions import db
from app.utils.enums import TransactionTypeEnum, TransactionStatusEnum


class TransactionModel(db.Model):
    """
    Модель данных Транзакций в кошельке.
    """
    __tablename__ = 'transactions'

    ref = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment='PK: UUID (Уникальный идентификатор транзакции)'
    )
    wallet_ref = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('wallets.ref'),
        nullable=False,
        comment='FK: UUID(Кошелек в котором прошла транзакция)'
    )
    amount = db.Column(
        db.Numeric(12,2),
        nullable=False,
        comment='Numeric (Размер транзакции)'
    )
    type = db.Column(
        db.Enum(TransactionTypeEnum),
        nullable=False,
        default=TransactionTypeEnum.TRANSFER,
        comment='Enum(TransactionTypeEnum) - (Тип Транзакции)'
    )
    status = db.Column(
        db.Enum(TransactionStatusEnum),
        nullable=False,
        default=TransactionStatusEnum.PENDING,
        comment='Enum(TransactionStatusEnum) - (Статус Транзакции)'
    )
    description = db.Column(
        db.String(50),
        nullable=True,
        default=None,
        comment='String (Комментарий к транзакции)'
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        nullable=False,
        comment='DateTime (Дата и время проведения транзакции)'
    )
    wallet = db.relationship(
        'WalletModel',
        back_populates='transactions',
    )