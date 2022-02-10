# TODO доделать бд игрока. Добавить функциюю получение данных и занесения их и *удаление. Сделать тоже самое в клане. Или оно уже есть и сказать мне
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

from python.Static.cfg.cfg_postgres import *

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")

name_len = 10

Base = declarative_base()

Base.metadata.create_all(engine)
