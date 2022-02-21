from sqlalchemy import create_engine
from python.Static.cfg.cfg_postgres import *

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")
