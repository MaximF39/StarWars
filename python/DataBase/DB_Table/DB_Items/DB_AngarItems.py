from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DB_AngarItems(Base):
    __tablename__ = 'DB_AngarItems'

    id = Column(Integer, primary_key=True)
    ownerId = Column(BigInteger, ForeignKey('DB_BasePlayer.id'), unique=True)

    classNumber = Column(SmallInteger, nullable=False)
