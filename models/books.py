from models.book_subject import BookSubject
from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import List
from models.book_author import BookAuthor 
from models.book_language import BookLanguage
from .book_bookshelf import BookBookShelf
from .format import Format

class Book(Base):

    __tablename__ = "books_book"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    download_count: Mapped[int] = mapped_column(Integer, nullable = True)
    gutenberg_id: Mapped[int] = mapped_column(Integer, nullable = True)
    media_type: Mapped[str] = mapped_column(String(16))
    title: Mapped[str] = mapped_column(String(1024))
    authors = relationship("Author", secondary = BookAuthor.__tablename__, viewonly = True, lazy = "immediate")
    languages = relationship("Language", secondary = BookLanguage.__tablename__, viewonly = True, lazy = "immediate")
    subjects = relationship("Subject", secondary = BookSubject.__tablename__, viewonly = True, lazy = "immediate")
    bookshelves = relationship("BookShelf", secondary = BookBookShelf.__tablename__, viewonly = True, lazy = "immediate")
    download_links = relationship("Format", lazy = "immediate")

