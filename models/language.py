from .base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer



class Language(Base):

    __tablename__ = "books_language"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    code: Mapped[str] = mapped_column(String(4))
