from pydantic_settings import BaseSettings, SettingsConfigDict

class Core(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASS:str
    DB_NAME:str

    @property
    def engin_create_url(self):
        core_url = f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return core_url

    model_config = SettingsConfigDict(env_file='.env')

settings = Core()