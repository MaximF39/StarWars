from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from python.DataBase.DB_Table.engine import engine
from python.Static.cfg.cfg_main import max_len_description_clan
Base = declarative_base()

class DB_Clan(Base):
    __tablename__ = 'DB_Clan'

    id = Column(BigInteger, primary_key=True)

    leaderId = Column(BigInteger, nullable=False)
    # leaderName = Column(String(name_len), nullable=False) #
    name = Column(String(12), nullable=False)
    shortName = Column(String(4), nullable=False)
    description = Column(String(max_len_description_clan),  default='') # use Text

    members = relationship("DB_BasePlayer", backref='members')

    level = Column(SmallInteger, nullable=False)
    rating = Column(BigInteger, nullable=False)
    cash = Column(BigInteger, nullable=False)
    bonus = Column(Integer, nullable=False)

    type = Column(SmallInteger, nullable=False)

    aliance = Column(SmallInteger, nullable=False)
    race = Column(SmallInteger, nullable=False)

    enemies = Column(Text, default='[]')
    friends = Column(Text, default='[]')

    logoFileName = Column(Text, default='')

Base.metadata.create_all(engine)