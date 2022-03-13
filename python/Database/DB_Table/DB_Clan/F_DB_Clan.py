from sqlalchemy import Column, BigInteger, ForeignKey, String, SmallInteger, Integer, Text
from sqlalchemy.orm import relationship, backref

from python.Config.CFG_Clan.cfg_db_clan import max_len_name_clan, max_len_short_name_clan, max_len_description_clan
from ..association import association
from ..engine import Base

class DB_Clan(Base):
    __tablename__ = 'db_clans'

    id = Column(BigInteger, primary_key=True)

    leaderId = Column(Integer, ForeignKey('db_b_players.id'))
    leader = relationship('DB_B_Player', backref=backref('leader', uselist=False))  # clan to DB_Skill as one to one
    db_players = relationship('DB_Player', backref='clan', lazy=True)  # db_clans to db_players as one to many
    members = relationship(  # db_b_players to db_clans as many to many
        'DB_B_Player', secondary=association,
        back_populates='db_clans')

    name = Column(String(max_len_name_clan), nullable=False)
    shortName = Column(String(max_len_short_name_clan), nullable=False)
    description = Column(String(max_len_description_clan), default='')  # use Text
    level = Column(SmallInteger, nullable=False)
    rating = Column(BigInteger, nullable=False)
    cash = Column(BigInteger, default=0)
    bonus = Column(Integer, default=0)
    type = Column(SmallInteger, nullable=False)
    aliance = Column(SmallInteger, nullable=False)
    race = Column(SmallInteger, nullable=False)
    enemies = Column(Text, default='[]')
    friends = Column(Text, default='[]')
    logoFileName = Column(Text, default='')