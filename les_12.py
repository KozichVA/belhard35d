from sqlalchemy import Column, INT, VARCHAR, ForeignKey, BOOLEAN, DECIMAL

from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True )

class Product(Base):
    __table__ = 'products'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    prise = Column(DECIMAL(8, 2), default=1)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

