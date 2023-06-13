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

    def __init__(self, name, code, is_verified, is_enabled, verification_code):
        self.name = name
        self.code = code
        self.is_verified = is_verified
        self.is_enabled = is_enabled
        self.verification_code = verification_code
