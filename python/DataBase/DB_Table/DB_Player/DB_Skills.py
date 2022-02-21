from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from python.DataBase.DB_Table.engine import engine

Base = declarative_base()


class DB_Skills(Base):
    __tablename__ = 'DB_Skills'

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)

    baseplayerdb = relationship('BasePlayerId', secondary="DB_Player", backref='DB_Skills')

    KineticWeapons = Column(SmallInteger, default=0)
    EnergyWeapons = Column(SmallInteger, default=0)
    RocketWeapons = Column(SmallInteger, default=0)
    Mining = Column(SmallInteger, default=0)
    Repairing = Column(SmallInteger, default=0)
    Trading = Column(SmallInteger, default=0)
    Control = Column(SmallInteger, default=0)
    Defending = Column(SmallInteger, default=0)
    Attacking = Column(SmallInteger, default=0)
    Tactics = Column(SmallInteger, default=0)
    Piloting = Column(SmallInteger, default=0)
    Targeting = Column(SmallInteger, default=0)
    Electronics = Column(SmallInteger, default=0)
    Cybernetics = Column(SmallInteger, default=0)
    Mechanics = Column(SmallInteger, default=0)
    Biocemistry = Column(SmallInteger, default=0)


def init():
    Base.metadata.create_all(engine)
