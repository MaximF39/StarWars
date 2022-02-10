from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

name_len = 10

class ClanDB(Base):
    __tablename__ = 'ClanDB'

    id = Column(Integer, primary_key=True)

    leaderId = Column(Integer, nullable=False)
    leaderName = Column(String(name_len), nullable=False)
    members = Column(Text, default='[]') # id, role
    name = Column(String(12), nullable=False)
    shortName = Column(String(4), nullable=False)
    description = Column(String(1000),  default='') # use Text
    level = Column(SmallInteger, nullable=False)
    rating = Column(Integer, nullable=False)
    cash = Column(BigInteger, nullable=False)
    bonus = Column(SmallInteger, nullable=False)
    type = Column(SmallInteger, nullable=False)
    repository = Column(Text, default='[]')
    aliance = Column(SmallInteger, nullable=False)
    race = Column(SmallInteger, nullable=False)
    enemies = Column(Text, default='[]')
    friends = Column(Text, default='[]')
    logoFileName = Column(Text, default='')
