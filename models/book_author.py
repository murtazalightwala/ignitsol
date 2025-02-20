from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from .author import Author

class BookAuthor(Base):

    __tablename__ = "books_book_authors"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books_book.id"))
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("books_author.id"))
    author = relationship("Author", foreign_keys = author_id)
    book = relationship("Book", foreign_keys = book_id)

