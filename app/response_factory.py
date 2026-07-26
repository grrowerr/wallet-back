from flask import jsonify


class ResponseFactory:
    """
    Фабрика, формирующая единообразные JSON-ответы API.
    """

    @staticmethod
    def success(data: dict, message: str = 'OK', status_code: int=200):
        payload = {
            'success': True,
            'data': data,
            'message': message,
            'errors': None
        }
        return jsonify(payload), status_code

    @staticmethod
    def error(message: str = 'ERROR', error=None, status_code: int=400):
        payload = {
            'success': False,
            'data': None,
            'message': message,
            'errors': error
        }
        return jsonify(payload), status_code

