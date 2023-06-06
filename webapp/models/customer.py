from .model_base import AppModelBase, nn_column

from .model_mixins import AutoIdModelMixin, AuditModelMixin, NameModelMixin, TenantBasedModelMixin

from sqlalchemy import Column, Text


class Customer(AppModelBase, AutoIdModelMixin, NameModelMixin, TenantBasedModelMixin, AuditModelMixin):
    __tablename__ = 'customers'

    address = Column(Text)
    phone = nn_column(Text)
    email = Column(Text)
