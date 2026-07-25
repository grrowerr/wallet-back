import enum


class TransactionTypeEnum(enum.Enum):
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'
    TRANSFER = 'TRANSFER'
