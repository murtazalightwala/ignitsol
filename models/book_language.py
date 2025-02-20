from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from models.language import Language

class BookLanguage(Base):

    __tablename__ = "books_book_languages"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books_book.id"))
    language_id: Mapped[int] = mapped_column(Integer, ForeignKey("books_language.id"))
    book = relationship("Book", foreign_keys = book_id)
    language = relationship("Language", foreign_keys = language_id)

