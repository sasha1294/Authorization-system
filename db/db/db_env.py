from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

DB_HOST='localhost'
DB_PORT=5432
DB_USER='postgres'
DB_PASS=123
DB_NAME='postgres'
core = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engin = create_engine(url=core,
                      echo=True)

Session = sessionmaker(bind=engin)
session = Session()

class Base(DeclarativeBase):
    pass

def create_base():
    Base.metadata.create_all(bind=engin)



