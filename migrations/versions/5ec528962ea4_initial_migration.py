"""Initial migration.

Revision ID: 5ec528962ea4
Revises: 
Create Date: 2023-06-06 17:56:22.165884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ec528962ea4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tenants',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=False),
    sa.Column('verification_code', sa.Text(), nullable=False),
    sa.Column('code', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tenants'))
    )
    op.create_table('customers',
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('phone', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.Column('modified_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name=op.f('fk_customers_tenant_id_tenants')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_customers'))
    )
    op.create_table('product_categories',
    sa.Column('parent_category_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_category_id'], ['product_categories.id'], name=op.f('fk_product_categories_parent_category_id_product_categories')),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name=op.f('fk_product_categories_tenant_id_tenants')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_categories'))
    )
    op.create_table('orders',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.Column('modified_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_orders_customer_id_customers')),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name=op.f('fk_orders_tenant_id_tenants')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_orders'))
    )
    op.create_table('products',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('tenant_id', sa.Integer(), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.Column('modified_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['product_categories.id'], name=op.f('fk_products_category_id_product_categories')),
    sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name=op.f('fk_products_tenant_id_tenants')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_products'))
    )
    op.create_table('order_items',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_order_items_order_id_orders')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_order_items_product_id_products')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order_items'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('product_categories')
    op.drop_table('customers')
    op.drop_table('tenants')
    # ### end Alembic commands ###