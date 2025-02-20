from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer



class Author(Base):

    __tablename__ = "books_author"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    birth_year: Mapped[int] = mapped_column(Integer, nullable = True)
    death_year: Mapped[int] = mapped_column(Integer, nullable = True)
    name: Mapped[str] = mapped_column(String(128))
