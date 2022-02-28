from sqlalchemy import Column, BigInteger, ForeignKey, String, SmallInteger, Integer, Text
from sqlalchemy.orm import relationship

from python.Config.CFG_Clan.cfg_db_clan import max_len_name_clan, max_len_short_name_clan, max_len_description_clan
from ..engine import Base

class db_clan(Base):
    __tablename__ = 'db_clans'

    id = Column(BigInteger, primary_key=True)
    leaderId = Column(BigInteger, ForeignKey('db_players.id'))
    leaderName = Column(BigInteger, ForeignKey('db_players.login'))

    # members = relationship("db_player")

    # leader = relationship("db_player", back_populates="clan", uselist=False)

    name = Column(String(max_len_name_clan), nullable=False)
    shortName = Column(String(max_len_short_name_clan), nullable=False)
    description = Column(String(max_len_description_clan), default='')  # use Text

    # members = relationship("DB_BasePlayer", backref='members')

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