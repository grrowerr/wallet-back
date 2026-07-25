import datetime
import uuid

from sqlalchemy.dialects.postgresql.base import UUID

from app.extensions import db
from app.utils.enums import CurrencyEnum


class WalletModel(db.Model):
    """
    Модель данных кошелька.
    """
    __tablename__ = 'wallets'

    ref = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        comment='PK: UUID (Уникальный идентификатор кошелька)'
    )
    balance = db.Column(
        db.Numeric(12, 2),
        nullable=False,
        default=0,
        comment='Numeric (Баланс кошелька)'
    )
    currency = db.Column(
        db.Enum(CurrencyEnum),
        nullable=False,
        default=CurrencyEnum.RUB,
        comment='Enum(Currency) - (Валюта)'
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now(),
        nullable=False,
        comment='DateTime (Дата и время создания кошелька)'
    )
    updated_at = db.Column(
        db.DateTime,
        nullable=True,
        default=None,
        onupdate=datetime.datetime.now,
        comment='DateTime(Дата последней транзакции).'
    )
    transactions = db.relationship(
        'TransactionModel',
        back_populates='wallet',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )
