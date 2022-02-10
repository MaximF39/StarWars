from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

name_len = 10

Base = declarative_base()

class ItemsDB(Base):
    __tablename__ = 'ItemsDB'

    key = Column(BigInteger, primary_key=True)

