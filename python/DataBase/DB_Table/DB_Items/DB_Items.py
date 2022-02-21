from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DB_Items(Base):
    __tablename__ = 'DB_Items'
    guid = Column(BigInteger, primary_key=True, unique=True)

    ownerId = Column(BigInteger, ForeignKey('DB_BasePlayer.id'), unique=True)
    where = Column(SmallInteger, nullable=False)

    classNumber = Column(SmallInteger, nullable=False)
    wear = Column(Integer, nullable=False)

    type = Column(SmallInteger, nullable=False)
    inUsing = Column(Boolean, default=False)
