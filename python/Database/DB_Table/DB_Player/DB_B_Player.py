from sqlalchemy import Integer, String, Column, SmallInteger, BigInteger, Boolean
from sqlalchemy.orm import relationship

from python.Config.CFG_Player.cfg_db_player import max_len_name, max_len_passwd
from python.Database.DB_Table.association import association
from python.Database.DB_Table.engine import Base


class DB_B_Player(Base):
    __tablename__ = 'db_b_players'
    id = Column(BigInteger, primary_key=True)

    login = Column(String(max_len_name), nullable=False, unique=True)
    password = Column(String(max_len_passwd), nullable=False)

    db_players = relationship('DB_Player', backref='player', lazy=True)
    db_clans = relationship(
        'DB_Clan', secondary=association,
        back_populates='members', lazy=True
    )

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
    class_number = Column(SmallInteger, nullable=False)
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