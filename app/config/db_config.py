class DBConfig:
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = '123qweasd'
    DB_HOST: str = 'localhost'
    DB_PORT: str = '5432'
    DB_NAME: str = 'wallet_back'

    # noinspection pep8-naming,SpellCheckingInspection
    @property
    def DB_URI(self) -> str:
        __db_uri = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            db_name=self.DB_NAME
        )
        return __db_uri
