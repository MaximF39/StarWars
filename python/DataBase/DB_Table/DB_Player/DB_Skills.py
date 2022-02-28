from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from python.DataBase.DB_Table.engine import engine

Base = declarative_base()
from ..engine import Base

class db_skill(Base):
    __tablename__ = 'db_skills'
    ownerId = Column(BigInteger, ForeignKey('db_players.id'), primary_key=True)

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
