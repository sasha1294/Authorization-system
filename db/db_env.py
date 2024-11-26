from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.config import settings
from sqlalchemy.orm import DeclarativeBase

engin = create_engine(url=settings.engin_create_url,
                      echo=True)

Session = sessionmaker(bind=engin)
session = Session()

class Base(DeclarativeBase):
    pass

def create_base():
    Base.metadata.drop_all(bind=engin)
    Base.metadata.create_all(bind=engin)




