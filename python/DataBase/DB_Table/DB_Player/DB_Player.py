from sqlalchemy import Column, BigInteger, ForeignKey, SmallInteger, String, Boolean
from sqlalchemy.orm import relationship

from python.Config.CFG_Player.cfg_db_player import max_len_name, max_len_passwd
from ..engine import Base

class db_player(Base):
    __tablename__ = 'db_players'

    id = Column(BigInteger, primary_key=True)
    login = Column(String(max_len_name), nullable=False, unique=True)
    password = Column(String(max_len_passwd), nullable=False)
    skills = relationship("db_skill", uselist=False)

    clanId = Column(BigInteger, ForeignKey('db_clans.id'), default=0)

    clan = relationship("db_clan", uselist=False)
    items = relationship("db_item")

    cash = Column(BigInteger, default=0)
    bonus = Column(SmallInteger, default=0)
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