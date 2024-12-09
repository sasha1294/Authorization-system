class Core():
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_USER = "postgres"
    DB_PASS = 123
    DB_NAME = "postgres"

    @property
    def engin_create_url(self):
        core_url = f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return core_url

