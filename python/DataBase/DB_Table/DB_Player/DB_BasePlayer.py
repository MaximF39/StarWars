from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from python.Static.cfg.cfg_main import max_len_name, max_len_passwd
from python.DataBase.DB_Table.engine import engine

Base = declarative_base()

# items
"""
repository = relationship("RepositoryItemsDB", backref='repository')
activeDevices = Column(Text, default='[]')
activeWeapons = Column(Text, default='[]')
inventory = relationship("InventoryItemsDB", backref='inventory')
angar = Column(Text, default='[]')
engineId = Column(SmallInteger, default=14)
"""


class DB_BasePlayer(Base):
    __tablename__ = 'DB_BasePlayer'

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)

    skillsdb = relationship('DB_Skills', secondary="DB_Player", backref='DB_BasePlayer')

    login = Column(String(max_len_name), nullable=False, unique=True)
    passwd = Column(String(max_len_passwd), nullable=False)
    cash = Column(BigInteger, default=0)
    bonus = Column(SmallInteger, default=0)
    clanId = Column(BigInteger, ForeignKey('DB_Clan.id'), default=0)
    spaceObjectId = Column(SmallInteger, default=0)
    locationId = Column(SmallInteger, nullable=False)
    clanRequestStatus = Column(SmallInteger, default=0)
    clanJoinRequestStatus = Column(SmallInteger, default=0)
    PlayerRelation = Column(SmallInteger, default=0)
    race = Column(SmallInteger, nullable=False)
    avatar = Column(SmallInteger, nullable=False)
    aliance = Column(SmallInteger, nullable=False)
    role = Column(SmallInteger, default=0)
    classNumber = Column(SmallInteger, nullable=False)
    x = Column(SmallInteger, nullable=True)
    y = Column(SmallInteger, nullable=True)
    count_reset_skills = Column(SmallInteger, default=0)
    isAdmin = Column(Boolean, default=False)
    deleteEnqueued = Column(Boolean, default=False)
    canDelete = Column(Boolean, default=False)
    rating = Column(BigInteger, default=0)
    experience = Column(BigInteger, default=0)
    points = Column(BigInteger, default=0)
    expSkillGrowCoef = Column(SmallInteger, default=2)
    expSkillReduserCoef = Column(SmallInteger, default=10)


def init():
    Base.metadata.create_all(engine)
