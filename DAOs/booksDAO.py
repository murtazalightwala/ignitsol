from typing import List, Optional

from fastapi import Query
from sqlalchemy import literal_column, or_

from models import language
from models.author import Author
from models.format import Format
from .baseDAO import BaseSQLDAO, BaseSQLListingQuery, BaseSQLSort, SortOrder
from models.books import Book
from models.language import Language
from models.subject import Subject
from models.bookshelf import BookShelf



class BookSearch(BaseSQLListingQuery):

    book_id: Optional[str | None] = Query(None)
    language: Optional[str | None] = Query(None)
    mime_type: Optional[str | None] = Query(None)
    topic: Optional[str | None] = Query(None)
    author: Optional[str | None] = Query(None)
    title: Optional[str | None]  = Query(None)

    def apply_filters(self, query_object, dao, *args, **kwargs):
        
        d = self.dict(exclude_none = True)

        for k, v in d.items():
            try:
                column = getattr(dao._model_class, k)
            except:
                pass
            if k == "book_id":
                column = getattr(dao._model_class, "gutenberg_id")
                vals = [x.strip() for x in v.split(",")]
                if len(vals) == 1:
                    query_object = query_object.filter(column == vals[0])
                else:
                    query_object = query_object.filter(column.in_(vals))
            elif k == "language":
                column = getattr(dao._model_class, "languages")
                vals = [x.strip() for x in v.split(",")]
                if len(vals) == 1:
                    query_object = query_object.filter(column.any(code = vals[0]))
                else:
                    query_object = query_object.filter(column.any(Language.code.in_(vals)))
            elif k == "topic":
                subject_column = getattr(dao._model_class, "subjects")
                bookshelf_column = getattr(dao._model_class, "bookshelves")
                vals = [x.strip() for x in v.split(",")]
                if len(vals) == 1:
                    query_object = query_object.filter(or_(subject_column.any(Subject.name.ilike(f"%{vals[0]}%")), bookshelf_column.any(BookShelf.name.ilike(f"%{vals[0]}%"))))
                else:
                    for val in vals:
                        query_object = query_object.filter(or_(subject_column.any(Subject.name.ilike(f"%{val}%")), bookshelf_column.any(BookShelf.name.ilike(f"%{val}%"))))
            elif k == "mime_type":
                column = getattr(dao._model_class, "download_links")
                vals = [x.strip() for x in v.split(",")]
                if len(vals) == 1:
                    query_object = query_object.filter(column.any(mime_type = vals[0]))
                else:
                    query_object = query_object.filter(column.any(Format.mime_type.in_(vals)))
            elif k == "title":
                vals = [x.strip() for x in v.split(",")]
                if len(vals) == 1:
                    query_object = query_object.filter(column.ilike(f"%{vals[0]}%"))
                else:
                    query_object = query_object.filter(or_(*[column.ilike(f"%{val}%") for val in vals]))
            elif k == "author":
                column = getattr(dao._model_class, "authors")
                vals = [x.strip() for x in v.split(",")]
                if len(vals) == 1:
                    query_object = query_object.filter(column.any(Author.name.ilike(f"%{vals[0]}%")))
                else:
                    query_object.filter(or_(*[column.any(Author.name.ilike(f"%{val}%")) for val in vals]))
        return query_object


class BookSort(BaseSQLSort):
    sort_by_download_count: SortOrder = Query(SortOrder.desc)


class Ts(BaseSQLListingQuery):

    book_id: int = Query(None)

class BooksDAO(BaseSQLDAO):

    _model_class = Book
    pk = "id"


