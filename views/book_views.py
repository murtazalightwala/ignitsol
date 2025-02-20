from fastapi import APIRouter, HTTPException, Depends
from DAOs.baseDAO import QueryStatus
from DAOs.booksDAO import BooksDAO, BookSearch, BookSort
from utils.paginator import LimitOffsetPaginator
import json

books_router = APIRouter(prefix = "/books", tags = ["books"])

@books_router.get("/search")
async def search_book(search_fields: BookSearch = Depends(), paginator: LimitOffsetPaginator = Depends(), sort: BookSort = Depends()):
    _dao_list = BooksDAO().list(skip = paginator.offset, limit = paginator.limit, filter = search_fields)
    if _dao_list.status == QueryStatus.success:
        return _dao_list.data
    else:
        raise HTTPException(status_code = 400, detail = {"status": _dao_list.status, "error": _dao_list.error})



@books_router.get("/{id}")
async def get_book_by_id(id):
    _dao_get = BooksDAO().get(id)
    if _dao_get.status == QueryStatus.success:
        return _dao_get.data
    else:
        print("ho ho ho !!!")
        raise HTTPException(status_code = 400, detail = {"status": _dao_get.status, "error": _dao_get.error})



