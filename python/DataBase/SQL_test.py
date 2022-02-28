from python.DataBase.DB_Table.DB_Player.DB_Player import db_player
from python.DataBase.DB_Table.DB_Player.DB_Skills import db_skill
from python.DataBase.DB_Table.DB_Clan.DB_Clan import db_clan
from python.DataBase.DB_Table.DB_Items.DB_Items import db_item
from python.DataBase.DB_Table.DB_Items.DB_AngarItems import db_angar
from python.DataBase.DB_Table.engine import *


def create_player():
    player = db_player(
        login="login",
        password="passwd",
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
    clan = db_clan(
        name='AdminClan',
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
    items = db_item(guid="2498jd32nd2",
                    classNumber=4,
                    where=1,
                    wear=100,
                    inUsing=False)
    angar = db_angar(classNumbers=12)
    skills = db_skill()

    player.clan = [clan]
    player.skills = [skills]
    player.angar = [angar]
    player.items = [items]

    s.add(player)
    s.add(clan)
    s.add(skills)
    s.add(items)
    s.commit()


def create_tables():
    db_player.__table__.create(engine)
    db_skill.__table__.create(engine)
    db_clan.__table__.create(engine)
    db_angar.__table__.create(engine)
    db_item.__table__.create(engine)


def main():
    create_tables()
    create_player()
