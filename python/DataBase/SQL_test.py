from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from DB_Table.DB_Player import DB_BasePlayer
from DB_Table.DB_Player import DB_Skills

def create_player():

    player = DB_BasePlayer.DB_BasePlayer(
        login="login",
        passwd="passwd",
        # clan=1,
        cash=5000000,
        bonus=5000,
        locationId=7,
        experience=468770,
        # clanRequestStatus=
        # clanJoinRequestStatus=
        # PlayerRelation=
        race=3,
        avatar=2001,
        aliance=3,
        rating=50000,
        role=1,
        classNumber=5999,
        # expSkillGrowCoef=
        # expSkillReduserCoef=
        points=6000,
        x=0,
        y=0,
        # deleteEnqueued=
        # canDelete=
    )
    send_commit(player)

def create_clan():
    clan = ClanDB(
        leaderId=255,
        clanId=1,
        name='AdminClan',
        leaderName='Admin',
        shortName='CLAN',
        description='description',
        level=1,
        rating=19000,
        cash=0,
        bonus=0,
        type=1,
        aliance=2,
        race=2,
        enemies=str([]),
        friends=str([]),
        logoFileName='',
    )

    send_commit(clan)

def send_commit(data):
    s.add(data)
    s.commit()

def drop_all():
    Base = declarative_base()
    Base.metadata.drop_all(engine)

def init():
    DB_BasePlayer.init()
    DB_Skills.init()

if __name__ == '__main__':
    host = "127.0.0.1"
    db_name_user = "postgres"
    db_passwd_user = "123"
    db_name = "test_main"
    port = 5432

    debug = False
    engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}", echo=debug)
    # init()
    session = sessionmaker(bind=engine)
    s = session()

    # create_clan()
    create_player()
