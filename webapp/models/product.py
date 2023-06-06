from .model_base import AppModelBase, nn_column

from .model_mixins import AutoIdModelMixin, AuditModelMixin, NameModelMixin, TenantBasedModelMixin

from sqlalchemy import Column, Text, Integer, ForeignKey, Float


class ProductCategory(AppModelBase, AutoIdModelMixin, NameModelMixin, TenantBasedModelMixin):
    __tablename__ = 'product_categories'

    parent_category_id = Column(Integer, ForeignKey('product_categories.id'))


class Product(AppModelBase, AutoIdModelMixin, NameModelMixin, TenantBasedModelMixin, AuditModelMixin):
    __tablename__ = 'products'

    category_id = nn_column(Integer, ForeignKey(ProductCategory.id))
    price = Column(Float)
