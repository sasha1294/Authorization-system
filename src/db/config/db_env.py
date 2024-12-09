from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = "postgres"
DB_PASS = 123
DB_NAME = "postgres"
core_url = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engin = create_async_engine(url=core_url,
                      echo=True)

Session = async_sessionmaker(bind=engin)
session = Session()

Base = declarative_base()

async def create_base():
    async with engin.begin() as engin_async:
        await engin_async.run_sync(Base.metadata.drop_all)
        await engin_async.run_sync(Base.metadata.create_all)