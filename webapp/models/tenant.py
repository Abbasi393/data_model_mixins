from .model_base import AppModelBase, nn_column
from .model_mixins import CodeModelMixin

from sqlalchemy import Column, Text, Integer, Boolean


class Tenant(AppModelBase, CodeModelMixin):
    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = nn_column(Text)
    is_verified = nn_column(Boolean, default=False)
    is_enabled = nn_column(Boolean, default=False)
    verification_code = nn_column(Text)
