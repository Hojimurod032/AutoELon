from sqlalchemy import create_engine, Column, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column # noqa
from Data.config import DB_URL


engine = create_engine(DB_URL)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'userss'
    id : Mapped[int] = Column(Integer, primary_key=True)
    tg_id : Mapped[int] = mapped_column( BigInteger , unique=True)
    name: Mapped[str]
    age: Mapped[int]
    number: Mapped[str] = mapped_column(unique=True)

class Cars(Base):
    __tablename__ = 'cars'
    id : Mapped[int] = Column(Integer, primary_key=True)
    title : Mapped[str]
    age : Mapped[int]
    price : Mapped[float]
    user_number : Mapped[str]
    user_id: Mapped[int] = mapped_column(BigInteger,ForeignKey("userss.tg_id"))
Base.metadata.create_all(engine)
