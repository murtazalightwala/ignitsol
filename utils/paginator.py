from pydantic import BaseModel
from fastapi import Query


class LimitOffsetPaginator(BaseModel):
    offset: int = Query(0, ge = 0)
    limit: int = Query(25, gt = 9, lt = 100)



