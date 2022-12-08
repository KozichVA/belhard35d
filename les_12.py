from sqlalchemy import Column, INT, VARCHAR, ForeignKey, BOOLEAN, DECIMAL

from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True )

class Product(Base):
    __tablename__ = 'products'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    prise = Column(DECIMAL(8, 2), default=1)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

class Status(Base):
    __tablename__ = 'statuses'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(10), unique=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24))
    email = Column(VARCHAR(24), unique=True)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(INT, primary_key=True)
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'))
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='CASCADE'))

class Order_item(Base):
    __tablename__ = 'order_items'
    id = Column(INT, primary_key=True)
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'))
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'))



