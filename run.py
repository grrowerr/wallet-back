from app import wallet_app


if __name__ == '__main__':
    wallet_app.debug = True
    wallet_app.run(host='0.0.0.0', port=5000)
