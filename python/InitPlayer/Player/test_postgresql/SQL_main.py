from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import psycopg2
from cfg import *

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}", echo=True)

Base = declarative_base()

# TODO доделать бд игрока. Добавить функциюю получение данных и занесения их и *удаление. Сделать тоже самое в клане. Или оно уже есть и сказать мне
class PlayerDB(Base):
    __tablename__ = 'PlayerDB'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    auth_key = Column(String(32), nullable=False)
    passwd = Column(String(32), nullable=False) # желательно тип хэш, если есть
    clan_id = Column(SmallInteger)
    credit = Column(BigInteger, nullable=False)
    bonus = Column(SmallInteger, nullable=False)
    planet = Column(SmallInteger)
    location = Column(SmallInteger, nullable=False)
    lvl_exp = Column(SmallInteger, nullable=False)
    count_exp = Column(BigInteger, nullable=False)
    lvl_stat = Column(SmallInteger, nullable=False)
    count_stat = Column(BigInteger, nullable=False)
    book = relationship("Book")  # 1 ко многим
    # сделать по клану связь игрока и в каком он клане

class ClanDB(Base):
    __tablename__ = 'ClanDB'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    short_name = Column(String(4), nullable=False)
    description = Column(String(1000)) # use Text
    level = Column(SmallInteger, nullable=False)
    count_exp = Column(SmallInteger, nullable=False)
    credit = Column(BigInteger, nullable=False)
    bonus = Column(SmallInteger, nullable=False)
    type = Column(SmallInteger, nullable=False)


    book = relationship("Book")  # 1 ко многим


Base.metadata.create_all(engine)
