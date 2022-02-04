from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from python.Static.cfg.cfg_postgres import *

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")

name_len = 10

Base = declarative_base()

# TODO доделать бд игрока. Добавить функциюю получение данных и занесения их и *удаление. Сделать тоже самое в клане. Или оно уже есть и сказать мне
class PlayerDB(Base):
    __tablename__ = 'PlayerDB'

    key = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=False)
    login = Column(String(name_len), nullable=False)
    authKey = Column(String(32), nullable=False)
    cash = Column(BigInteger, nullable=False)
    bonus = Column(SmallInteger, nullable=False)

    repository = Column(Text, default='[]')

    clanId = Column(SmallInteger, default=0)
    spaceObjectId = Column(SmallInteger,  default=0)
    locationId = Column(SmallInteger, nullable=False)
    clanRequestStatus = Column(SmallInteger, default=0)
    clanJoinRequestStatus = Column(SmallInteger, default=0)

    PlayerRelation = Column(SmallInteger, default=0)
    race = Column(SmallInteger, nullable=False)
    avatar = Column(SmallInteger, nullable=False)
    aliance = Column(SmallInteger, nullable=False)
    role = Column(SmallInteger, default=0)

    classNumber = Column(SmallInteger, nullable=False)

    x = Column(SmallInteger, nullable=True) # Если есть Спасе обжект
    y = Column(SmallInteger, nullable=True) # Если на планете

    activeDevices = Column(Text, default='[]')
    activeWeapons = Column(Text, default='[]')
    engineId = Column(SmallInteger, default=14)

    inventory = Column(Text, default='[]')
    angar = Column(Text, default='[]')
    count_reset_skills = Column(SmallInteger, default=0)
    skills = Column(Text, nullable=False)

    isAdmin = Column(Boolean, default=False)
    deleteEnqueued = Column(Boolean, default=False)
    canDelete = Column(Boolean, default=False)
    logged = Column(Boolean, default=False)

    rating = Column(BigInteger, nullable=False)
    experience = Column(BigInteger, nullable=False)
    points = Column(BigInteger, default=0)

    expSkillGrowCoef = Column(SmallInteger, default=2)
    expSkillReduserCoef = Column(SmallInteger, default=10)

    # book = relationship("Book")  # 1 ко многим
    # сделать по клану связь игрока и в каком он клане

class ClanDB(Base):
    __tablename__ = 'ClanDB'

    key = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=False)
    leaderId = Column(Integer, primary_key=False)
    leaderName = Column(String(name_len), primary_key=False)
    members = Column(Text, default='[]') # id, role
    name = Column(String(12), nullable=False)
    shortName = Column(String(4), nullable=False)
    description = Column(String(1000),  default='') # use Text
    level = Column(SmallInteger, nullable=False)
    rating = Column(Integer, nullable=False)
    cash = Column(BigInteger, nullable=False)
    bonus = Column(SmallInteger, nullable=False)
    type = Column(SmallInteger, nullable=False)
    repository = Column(Text, default='[]')
    aliance = Column(SmallInteger, nullable=False)
    race = Column(SmallInteger, nullable=False)
    enemies = Column(Text, default='[]')
    friends = Column(Text, default='[]')
    logoFileName = Column(Text, default='')

    # book = relationship("Book")  # 1 ко многим

# class PlanetDB(Inventory):
#     __tablename__ = 'PlanetDB'
#
#     key = Column(Integer, primary_key=True)
#     id = Column(Integer, nullable=False)
#     players_id = Column(Text, default='[]') #
#     name = Column(String(12), nullable=False)
#     type = Column(SmallInteger, nullable=False)
#     shop = Column(Text, default='[]')
#     aliance = Column(SmallInteger, nullable=False)
#     race = Column(SmallInteger, nullable=False)


Base.metadata.create_all(engine)