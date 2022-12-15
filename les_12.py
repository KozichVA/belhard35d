from sqlalchemy import Column, INT, VARCHAR, ForeignKey, BOOLEAN, DECIMAL, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker, declarative_mixin, Session

Base = declarative_base()


@declarative_mixin
class Basemixin(object):
    engine = create_engine('postgresql://axlamon:axlamon@localhost:5432/newhomewok')
    _Session = sessionmaker(bind=engine)

    id = Column(INT, primary_key=True)

    @staticmethod
    def create_sesion(func):
        def wraper(*args, **kwargs):
            with Basemixin._Session() as session:
                return func(*args, **kwargs, session=session)
        return wraper

    @classmethod
    @create_sesion
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @classmethod
    @create_sesion
    def all(cls, order_by: str = 'id', session: Session = None, **kwargs):
        session.scalars(
            select(cls)
            .filter(**kwargs)
            .order_by(order_by)
        ).all()

    @create_sesion
    def save(self, session: Session = None) -> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @create_sesion
    def delete(self, session: Session = None) -> None:
        session.delete(self)
        session.commit()
class Category(Basemixin, Base):
    __tablename__ = 'categories'
    # id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True)


class Product(Basemixin, Base):
    __tablename__ = 'products'

    # id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    prise = Column(DECIMAL(8, 2), default=1)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class Status(Basemixin, Base):
    __tablename__ = 'statuses'
    # id = Column(INT, primary_key=True)
    name = Column(VARCHAR(10), unique=True)


class User(Basemixin, Base):
    __tablename__ = 'users'
    # id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24))
    email = Column(VARCHAR(24), unique=True)


class Order(Basemixin, Base):
    __tablename__ = 'orders'
    # id = Column(INT, primary_key=True)
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'))
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='CASCADE'))


class OrderItem(Basemixin, Base):
    __tablename__ = 'order_items'
    # id = Column(INT, primary_key=True)
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'))
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'))

    def __str__(self):
        return self.name



# Category.name = 'Холодильник'
Category.save()
print(Category.get(1))
