from typing import Any, List
from sqlalchemy.orm import query
from utils.db import get_db
from enum import Enum
from traceback import format_exc
from pydantic import BaseModel

class QueryStatus(str, Enum):
    success = "Success"
    failure = "Failure"


class DAOSuccess(BaseModel):
    status: QueryStatus = QueryStatus.success
    data: Any

class DAOFailure(BaseModel):
    status: QueryStatus = QueryStatus.failure
    error: str
    traceback: str

class BaseSQLListingQuery(BaseModel):

    def apply_filters(self, query_object, dao, *args, **kwargs):
        for k, v in self.dict(exclude_none = True).items():
            column = getattr(dao._model_class, k)
            query_object = query_object.filter(column == v)
        return query_object

class SortOrder(Enum):
    asc = "asc"
    desc = "desc"

class BaseSQLSort(BaseModel):

    def remove_prefix(self, t):
        return t[8:]

    def apply_sort(self, query_object, dao, *args, **kwargs):
        
        d = self.dict(exclude_none = True)

        for k, v in d.items():
            column = getattr(dao._model_class, self.remove_prefix(k))
            if v == SortOrder.asc:
                query_object = query_object.order_by(column)
            elif v == SortOrder.desc:
                query_object = query_object.order_by(column.desc())

        return query_object 

class BaseSQLDAO():
    
    db = next(get_db())

    def create(self, _obj, *args, **kwargs):
        try:
            self.db.add(_obj)
            self.db.commit()
            return DAOSuccess(data = _obj)
        except Exception as e:
            self.db.rollback()
            return DAOFailure(error = str(e), traceback = format_exc())

    def get(self, _id, *args, **kwargs):
        try:
            pk = getattr(self._model_class, self.pk)
            _object = self.db.query(self._model_class).filter(pk == _id).first()
            print(_object)
            return DAOSuccess(data = _object)
        except Exception as e:
            self.db.rollback()
            return DAOFailure(error = str(e), traceback = format_exc())

    def list(self, skip = 0, limit = 10, filter = BaseSQLListingQuery(), sort = BaseSQLSort(), *args, **kwargs):
        query = self.db.query(self._model_class)
        query = filter.apply_filters(query, self)
        query = sort.apply_sort(query, self)
        try:
            if limit != 0:
                data = query.offset(skip).limit(limit).all()
            else:
                data = query.offset(skip).all()
            if len(data) > 0:
                return DAOSuccess(data = data)
            else:
                return DAOFailure(error = "No Content", traceback = str(query.as_scalar()))
        except Exception as e:
            self.db.rollback()
            return DAOFailure(error = str(e), traceback = format_exc())

    def update(self, _id, _obj, *args, **kwargs):
        pass

    def delete(self, _id, _obj, *args, **kwargs):
        pass


