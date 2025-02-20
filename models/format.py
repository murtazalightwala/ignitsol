from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Integer



class Format(Base):

    __tablename__ = "books_format"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    mime_type: Mapped[str] = mapped_column(String(32))
    url: Mapped[str] = mapped_column(String(256))
    book_id: Mapped[int] = mapped_column(String(64), ForeignKey("books_book.id"))
