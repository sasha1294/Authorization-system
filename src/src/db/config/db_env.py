from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

engin = create_engine(url=f'postgresql+psycopg2://postgres:123@localhost:5432/postgres',
                      echo=True)

Session = sessionmaker(bind=engin)
session = Session()

class Base(DeclarativeBase):
    pass

def create_base():
    Base.metadata.drop_all(bind=engin)
    Base.metadata.create_all(bind=engin)