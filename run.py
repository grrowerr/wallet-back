from app import wallet_app


if __name__ == '__main__':
    wallet_app.debug = True
    wallet_app.run(host='127.0.0.1', port=5000)
