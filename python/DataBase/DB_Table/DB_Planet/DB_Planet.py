from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class DB_Planet(Base):
    __tablename__ = 'DB_Planet'

    key = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=False)
    players_id = Column(Text, default='[]') #
    # name = Column(String(12), nullable=False)
    type = Column(SmallInteger, nullable=False)
    aliance = Column(SmallInteger, nullable=False)
    race = Column(SmallInteger, nullable=False)
