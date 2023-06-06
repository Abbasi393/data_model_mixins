from .model_base import AppModelBase, nn_column
from webapp.models import Customer, Product
from .model_mixins import AutoIdModelMixin, AuditModelMixin, NameModelMixin, TenantBasedModelMixin

from sqlalchemy import Column, Text, Integer, ForeignKey, Float, DateTime


class Order(AppModelBase, AutoIdModelMixin, TenantBasedModelMixin, AuditModelMixin):
    __tablename__ = 'orders'

    customer_id = nn_column(Integer, ForeignKey(Customer.id))
    order_date = Column(DateTime)

    def calculate_total_price(self):
        return sum(item.product.price * item.quantity for item in self.order_items)


class OrderItem(AppModelBase, AutoIdModelMixin):
    __tablename__ = 'order_items'

    order_id = nn_column(Integer, ForeignKey(Order.id))
    product_id = Column(Integer, ForeignKey(Product.id))
    quantity = Column(Integer)
    price = Column(Float)
