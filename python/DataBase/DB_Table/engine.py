from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

host = "127.0.0.1"
db_name_user = "postgres"
db_passwd_user = "123"
db_name = "test_main"
port = 5432

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")

Base = declarative_base()
session = sessionmaker(bind=engine)()
s = session