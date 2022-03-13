from sqlalchemy import Column, BigInteger, ForeignKey, SmallInteger, String, Boolean, Integer
from sqlalchemy.orm import relationship

from python.Database.DB_Table.engine import Base

class DB_Player(Base):
    __tablename__ = 'db_players'

    id = Column(BigInteger, primary_key=True)

    clan_id = Column(Integer, ForeignKey('db_clans.id'), nullable=False)
    player_id = Column(Integer, ForeignKey('db_b_players.id'), nullable=False)

    items = relationship("DB_Item")
    angar = relationship("DB_Angar")

    skills_id = Column(Integer, ForeignKey('db_skills.id'), nullable=False)

