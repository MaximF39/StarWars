from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from python.DataBase.DB_Table.engine import engine


name_len = 10

Base = declarative_base()

#items
"""
repository = relationship("RepositoryItemsDB", backref='repository')
activeDevices = Column(Text, default='[]')
activeWeapons = Column(Text, default='[]')
inventory = relationship("InventoryItemsDB", backref='inventory')
angar = Column(Text, default='[]')
engineId = Column(SmallInteger, default=14)
"""

class DB_Player(Base):
    __tablename__ = 'DB_Player'
    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    skillsId = Column(BigInteger, ForeignKey('DB_Skills.id'), nullable=False)
    playerId = Column(BigInteger, ForeignKey('DB_BasePlayer.id'), nullable=False)


def init():
    Base.metadata.create_all(engine)