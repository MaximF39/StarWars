from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class SkillsDB(Base):
    __tablename__ = 'SkillsDB'

    id = Column(Integer, primary_key=True)

    player_id = Column(Integer, ForeignKey('PlayerDB.id'), unique=True)

    KineticWeapons = Column(SmallInteger, nullable=False)
    EnergyWeapons = Column(SmallInteger, nullable=False)
    RocketWeapons = Column(SmallInteger, nullable=False)
    Mining = Column(SmallInteger, nullable=False)
    Repairing = Column(SmallInteger, nullable=False)
    Trading = Column(SmallInteger, nullable=False)
    Control = Column(SmallInteger, nullable=False)
    Defending = Column(SmallInteger, nullable=False)
    Attacking = Column(SmallInteger, nullable=False)
    Tactics = Column(SmallInteger, nullable=False)
    Piloting = Column(SmallInteger, nullable=False)
    Targeting = Column(SmallInteger, nullable=False)
    Electronics = Column(SmallInteger, nullable=False)
    Cybernetics = Column(SmallInteger, nullable=False)
    Mechanics = Column(SmallInteger, nullable=False)
    Biocemistry = Column(SmallInteger, nullable=False)
