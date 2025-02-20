from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Integer
from .subject import Subject


class BookSubject(Base):

    __tablename__ = "books_book_subjects"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    book_id = mapped_column(Integer, ForeignKey("books_book.id"))
    subject_id = mapped_column(Integer, ForeignKey("books_subject.id"))
