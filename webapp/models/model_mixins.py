from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Boolean, Column, DateTime, Integer, Text, MetaData, ForeignKey, JSON
from .model_base import AppModelBase, nn_column


class AutoIdModelMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class NameModelMixin:
    name = nn_column(Text)


class TenantBasedModelMixin:
    @declared_attr
    def tenant_id(self):
        return nn_column(Integer, ForeignKey('tenants.id'))


class AuditModelMixin:
    is_enabled = nn_column(Boolean, default=True)

    created_on = nn_column(DateTime)
    created_by_id = nn_column(Integer)

    modified_on = Column(DateTime)
    modified_by_id = Column(Integer)


class SoftDeleteMixin:
    is_deleted = nn_column(Boolean, default=False)


class ApprovalMixin:
    approval_action = nn_column(Integer, default=0)  # 0 = Pending, 1 = Approved, 2 = Rejected
    approval_action_occurred_on = Column(DateTime)
    approval_action_done_by_id = Column(Integer)
    approval_action_remarks = Column(Text)


class VerifiedRecordMixin:
    is_verified = nn_column(Boolean, default=False)
    verified_action_occurred_on = Column(DateTime)
    verified_action_done_by_id = Column(Integer)


class CodeModelMixin:
    code = nn_column(Text)


class TagsModelMixin:
    tags = Column(Text)


class DictModelMixin:  # Just use for key value data
    id = nn_column(Integer, primary_key=True, autoincrement=False)
    name = nn_column(Text)
