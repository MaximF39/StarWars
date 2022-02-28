
from sqlalchemy import Column, BigInteger, ForeignKey, SmallInteger, String, Text, Integer, Boolean
from python.DataBase.DB_Table.engine import Base

class db_item(Base):
    __tablename__ = 'db_items'

    guid = Column(Text, primary_key=True, unique=True)

    ownerId = Column(BigInteger, ForeignKey('db_players.id'))

    where = Column(SmallInteger, nullable=False)

    classNumber = Column(SmallInteger, nullable=False)
    wear = Column(BigInteger, nullable=False)

    inUsing = Column(Boolean, default=False)

