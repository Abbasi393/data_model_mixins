from .model_base import AppModelBase, nn_column
from .model_mixins import AutoIdModelMixin, AuditModelMixin, NameModelMixin, TenantBasedModelMixin
from webapp.app import db
from sqlalchemy import Column, Text


class Customer(AppModelBase, AutoIdModelMixin, NameModelMixin, TenantBasedModelMixin, AuditModelMixin):
    __tablename__ = 'customers'

    address = Column(Text)
    phone = nn_column(Text)
    email = Column(Text)

    def __init__(self, name, address, phone, email, tenant_id, created_on,
                 created_by_id, is_enabled):
        self.name = name,
        self.address = address,
        self.phone = phone,
        self.email = email,
        self.tenant_id = tenant_id,
        self.created_on = created_on,
        self.created_by_id = created_by_id,
        self.is_enabled = is_enabled
