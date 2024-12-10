from sqlalchemy.orm import Mapped, mapped_column
from src.db.config.db_env import Base

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    country: Mapped[str] = mapped_column(nullable=False)


