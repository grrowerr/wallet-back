from uuid import UUID

from flask import Blueprint, request, jsonify

from app.response_factory import ResponseFactory
from app.wallet_api.crud.operation_crud import TransactionCRUD
from app.wallet_api.crud.wallet_crud import WalletCRUD

wallet_bp = Blueprint('wallet_bp', __name__, url_prefix='/api/v1/wallets')

transactionCRUD = TransactionCRUD()
walletCRUD = WalletCRUD()

@wallet_bp.post('<uuid:wallet_ref>/operation')
def create_operation(wallet_ref: UUID):
    """
    Для проведения операций с изменением баланса кошелька

    Поддерживает операции:
    DEPOSIT и WITHDRAW

    :param wallet_ref: (UUID) Уникальный идентификатор кошелька, с которым проводим операцию.
    """

    transaction_data = request.get_json()
    wallet_response_data = transactionCRUD.create(transaction_data=transaction_data, wallet_ref=wallet_ref)

    type = transaction_data.get('type')
    amount = transaction_data.get('amount')
    response, status_code = ResponseFactory.success(
        data=wallet_response_data,
        message=f'Операция {type}, Сумма операции: {amount}',
        status_code=201
    )

    return response, status_code

@wallet_bp.get('/<uuid:wallet_ref>')
def get_wallet_balance(wallet_ref: UUID):
    """
    Возвращает текущий баланс кошелька

    :param wallet_ref: (UUID) Уникальный идентификатор кошелька, баланс которого  возвращаем.
    """

    balance = walletCRUD.read_balance(wallet_ref=wallet_ref)
    response, status_code = ResponseFactory.success(
        data=balance,
    )

    return response, status_code
