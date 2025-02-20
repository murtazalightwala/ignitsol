from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer



class BookShelf(Base):

    __tablename__ = "books_bookshelf"
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    name: Mapped[str] = mapped_column(String(64))
