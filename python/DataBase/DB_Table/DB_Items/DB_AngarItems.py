from sqlalchemy import Column, BigInteger, ForeignKey, SmallInteger, String, Text
from python.DataBase.DB_Table.engine import Base

class db_angar(Base):
    __tablename__ = 'db_angars'

    id = Column(BigInteger, primary_key=True)

    ownerId = Column(BigInteger, ForeignKey('db_players.id'))

    classNumbers = Column(SmallInteger, nullable=False)
