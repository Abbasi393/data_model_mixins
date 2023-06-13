from datetime import datetime
from sqlalchemy import Column, MetaData
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

sa_metadata = MetaData(naming_convention=convention)
ModelBase = declarative_base(metadata=sa_metadata)


################################################################
# Helper functions
################################################################
def nn_column(*args, **kwargs):
    return Column(nullable=False, *args, **kwargs)


################################################################
# Base class for all Model objects
################################################################
class AppModelBase(ModelBase):
    __abstract__ = True

    def as_dict(self):
        try:
            result = {}
            for c in self.__table__.columns:
                col_value = getattr(self, c.name)
                if c.type.python_type == datetime:
                    col_value = str(col_value)
                result.update({c.name: col_value})
            return result
        except Exception as ex:
            print(ex)

    def __str__(self):
        return self.name
