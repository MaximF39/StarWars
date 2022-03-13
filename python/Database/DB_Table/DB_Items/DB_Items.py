
from sqlalchemy import Column, BigInteger, ForeignKey, SmallInteger, String, Text, Integer, Boolean
from sqlalchemy.orm import relationship

from python.Database.DB_Table.engine import Base

class DB_Item(Base):
    __tablename__ = 'db_items'

    guid = Column(Text, primary_key=True, unique=True)
    ownerId = Column(BigInteger, ForeignKey('db_players.id'))
    where = Column(SmallInteger, nullable=False)
    class_number = Column(SmallInteger, nullable=False)
    wear = Column(BigInteger, nullable=False)
    in_using = Column(Boolean, default=False)

