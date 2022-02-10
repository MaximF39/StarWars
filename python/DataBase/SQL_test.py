from sqlalchemy import create_engine
from sqlalchemy import func as sql_max
from sqlalchemy.orm import sessionmaker
from .DB.Player.PlayerDB import PlayerDB
from .DB.Player.SkillsDB import SkillsDB
from .DB.Clan.ClanDB import ClanDB
# from .cfg_postgres import *

host = "127.0.0.1"
db_name_user = "postgres"
db_passwd_user = "123"
db_name = "test_main"
port = 5432

debug = False
engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}", echo=debug)

# Флаг echo включает ведение лога через стандартный модуль logging Питона.
# Когда он включен, мы увидим все созданные нами SQL-запросы.
session = sessionmaker(bind=engine)
s = session()

def create_player():
    player = PlayerDB(
        id=255,
        login="Admin",
        authKey="authKey",
        clanId=1,
        cash=5000000,
        bonus=5000,
        # SpaceObject=
        locationId=7,
        experience=468770,
        angar=str([]),
        repository=str([]),
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
        # logged=
        activeWeapons=str([]),
        activeDevices=str([]),
    )
    s.add(player)
    s.commit()

    skills = SkillsDB(
        player_id=255,
        KineticWeapons = 1,
        EnergyWeapons = 1,
        RocketWeapons = 1,
        Mining = 1,
        Repairing = 1,
        Trading = 1,
        Control = 1,
        Defending = 1,
        Attacking = 1,
        Tactics = 1,
        Piloting = 1,
        Targeting = 1,
        Electronics = 1,
        Cybernetics = 1,
        Mechanics = 1,
        Biocemistry = 1,
    )
    s.add(skills)
    s.commit()


def create_clan():
    clan = ClanDB(
        leaderId=255,
        members='[{"id":255, "role":1}]',
        name='AdminClan',
        leaderName='Admin',
        shortName='CLAN',
        description='description',
        level=1,
        rating=19000,
        cash=0,
        bonus=0,
        type=1,
        repository=str([]),
        aliance=2,
        race=2,
        enemies=str([]),
        friends=str([]),
        logoFileName='',
    )

    s.add(clan)
    s.commit()

create_player()
create_clan()