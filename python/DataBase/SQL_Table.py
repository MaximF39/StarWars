from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# from .cfg_postgres import *

host = "127.0.0.1"
db_name_user = "postgres"
db_passwd_user = "123"
db_name = "test_main"
port = 5432

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")

Base = declarative_base()

# TODO доделать бд игрока. Добавить функциюю получение данных и занесения их и *удаление. Сделать тоже самое в клане. Или оно уже есть и сказать мне
class PlayerDB(Base):
    __tablename__ = 'PlayerDB'

    key = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=False)
    login = Column(String(10), nullable=False)
    auth_key = Column(String(32), nullable=False)
    passwd = Column(String(32), nullable=False) # желательно тип хэш, если есть
    clan_id = Column(SmallInteger, default=0)
    credit = Column(BigInteger, nullable=False)
    bonus = Column(SmallInteger, nullable=False)
    SpaceObject = Column(SmallInteger,  default=0)
    Location = Column(SmallInteger, nullable=False)
    repository = Column(Text, default='[]')
    level = Column(SmallInteger, nullable=False)
    experience = Column(BigInteger, nullable=False)
    status = Column(SmallInteger, nullable=False)
    clanRequestStatus = Column(SmallInteger, default=0)
    clanJoinRequestStatus = Column(SmallInteger, default=0)
    PlayerRelation = Column(SmallInteger, default=0)
    race = Column(SmallInteger, nullable=False)
    avatar = Column(SmallInteger, nullable=False)
    aliance = Column(SmallInteger, nullable=False)
    role = Column(SmallInteger, default=0)
    ship_class = Column(SmallInteger, nullable=False)
    skills = Column(Text, nullable=False)
    free_skills = Column(SmallInteger, default=0)
    expSkillGrowCoef = Column(SmallInteger, default=2)
    expSkillReduserCoef = Column(SmallInteger, default=10)
    point = Column(BigInteger, default=0)
    x = Column(SmallInteger, nullable=False)
    y = Column(SmallInteger, nullable=False)
    deleteEnqueued = Column(Boolean, default=False)
    canDelete = Column(Boolean, default=False)
    logged = Column(Boolean, default=False)
    active_devices = Column(Text, default='[]')
    active_weapons = Column(Text, default='[]')
    rating = Column(Integer, nullable=False)
    inventory = Column(Text, default='[]')
    angar = Column(Text, default='[]')

    # book = relationship("Book")  # 1 ко многим
    # сделать по клану связь игрока и в каком он клане
#
# class ClanDB(BaseClass):
#     __tablename__ = 'ClanDB'
#
#     id = Column(Integer, primary_key=True)
#     creator_id = Column(Integer, primary_key=False)
#     owner = Column(Integer, primary_key=False)
#     name = Column(String(10), nullable=False)
#     short_name = Column(String(4), nullable=False)
#     description = Column(String(1000),  default='') # use Text
#     level = Column(SmallInteger, nullable=False)
#     count_rating = Column(Integer, nullable=False)
#     credit = Column(BigInteger, nullable=False)
#     bonus = Column(SmallInteger, nullable=False)
#     type = Column(SmallInteger, nullable=False)


    # book = relationship("Book")  # 1 ко многим


Base.metadata.create_all(engine)
