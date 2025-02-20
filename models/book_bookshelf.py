from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from typing import List
from .bookshelf import BookShelf

class BookBookShelf(Base):

    __tablename__ = "books_book_bookshelves"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    book_id = mapped_column(Integer, ForeignKey("books_book.id"))
    bookshelf_id = mapped_column(Integer, ForeignKey("books_bookshelf.id"))

