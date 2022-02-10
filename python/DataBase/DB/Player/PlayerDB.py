from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

name_len = 10

Base = declarative_base()

class PlayerDB(Base):
    __tablename__ = 'PlayerDB'

    key = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=False, unique=True)
    login = Column(String(name_len), nullable=False)
    authKey = Column(String(32), nullable=False, unique=True)

    cash = Column(BigInteger, nullable=False)
    bonus = Column(SmallInteger, nullable=False)

    repository = Column(Text, default='[]')

    clanId = Column(SmallInteger, default=0)
    spaceObjectId = Column(SmallInteger,  default=0)
    locationId = Column(SmallInteger, nullable=False)
    clanRequestStatus = Column(SmallInteger, default=0)
    clanJoinRequestStatus = Column(SmallInteger, default=0)

    PlayerRelation = Column(SmallInteger, default=0)
    race = Column(SmallInteger, nullable=False)
    avatar = Column(SmallInteger, nullable=False)
    aliance = Column(SmallInteger, nullable=False)
    role = Column(SmallInteger, default=0)

    classNumber = Column(SmallInteger, nullable=False)

    x = Column(SmallInteger, nullable=True) # Если есть Спасе обжект
    y = Column(SmallInteger, nullable=True) # Если на планете

    activeDevices = Column(Text, default='[]')
    activeWeapons = Column(Text, default='[]')
    engineId = Column(SmallInteger, default=14)

    inventory = Column(Text, default='[]')
    angar = Column(Text, default='[]')
    count_reset_skills = Column(SmallInteger, default=0)
    skills = relationship("SkillsDB", backref='skills')

    isAdmin = Column(Boolean, default=False)
    deleteEnqueued = Column(Boolean, default=False)
    canDelete = Column(Boolean, default=False)
    logged = Column(Boolean, default=False)

    rating = Column(BigInteger, nullable=False)
    experience = Column(BigInteger, nullable=False)
    points = Column(BigInteger, default=0)

    expSkillGrowCoef = Column(SmallInteger, default=2)
    expSkillReduserCoef = Column(SmallInteger, default=10)
