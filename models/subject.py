from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer



class Subject(Base):

    __tablename__ = "books_subject"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    name: Mapped[str] = mapped_column(String(256))
