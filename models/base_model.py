from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect


class Base:

    def base_to_json(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


Base = declarative_base(cls = Base)

