import requests
from flask import Flask, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError, ProgrammingError

from app.extensions import db
from app.response_factory import ResponseFactory


def parse_integrity_error(e):
    orig_message = str(e.orig).lower()
    if 'unique' in orig_message or 'duplicate' in orig_message:
        return 'Запись с такими данными уже существует', {'type': 'unique_violation'}
    if 'foreign_key' in orig_message:
        return ('Нарушение связи с другой таблицей (Запись используется или не существует)',
                {'type': 'foreign_key_violation'})
    if 'not_null' in orig_message:
        return 'Не заполнено обязательное поле', {'type': 'not_null_violation'}
    return 'Ошибка целостности данных', {'type': 'integrity_error', 'detail': orig_message}

def register_error_handlers(app: Flask):
    """
    Регистрируем  глобальные обработчики ошибок.
    """
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        app.logger.exception(e)
        error_response = ResponseFactory.error(
            message='Ошибка при валидации',
            error=str(e)
        )
        return error_response

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        db.session.rollback()
        app.logger.exception(e)

        message, error = parse_integrity_error(e)
        error_response = ResponseFactory.error(
            message=message,
            error=error,
            status_code=409
        )
        return error_response

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        app.logger.exception(e)
        error_response = ResponseFactory.error(
            message='Internal server error',
            status_code=500
        )
        return error_response

    @app.errorhandler(ProgrammingError)
    def handle_insufficient_privilege(e):
        db.session.rollback()
        app.logger.exception(e)
        error_response = ResponseFactory.error(
            message='Ошибка при выполнении запроса к БД.',
            status_code=500
        )
        return error_response

    @app.errorhandler(ValueError)
    def handle_value_error(e):
        app.logger.exception(e)
        error_response = ResponseFactory.error(
            message=str(e),
        )
        return error_response

    @app.errorhandler(TypeError)
    def handle_type_error(e):
        app.logger.exception(e)
        error_response = ResponseFactory.error(
            message=str(e)
        )
        return error_response

    @app.errorhandler(requests.Timeout)
    def handle_timeout_error(e):
        app.logger.exception(e)
        error_response = ResponseFactory.error(
            message='Превышено время ожидания ответа.',
            error='Timeout Error',
            status_code=504
        )

    @app.errorhandler(requests.ConnectionError)
    def handle_connection_error(e):
        app.logger.exception(e)
        error_response = ResponseFactory.error(
            message='Ошибка соединения.',
            error='Connection Error',
            status_code=503
        )
