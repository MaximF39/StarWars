from python.Database.Database import DataBase
from python.Database.DB_Table.engine import *
from python.Database.DB_Table.DB_Player.DB_B_Player import DB_B_Player
from python.Database.DB_Table.DB_Player.DB_Skills import DB_Skill
from python.Database.DB_Table.DB_Clan.F_DB_Clan import DB_Clan
from python.Database.DB_Table.DB_Items.DB_Items import DB_Item
from python.Database.DB_Table.DB_Items.DB_Angar import DB_Angar
from python.Database.DB_Table.DB_Player.F_DB_Player import DB_Player


def create_player():
    b_player = DB_B_Player(
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
        class_number=5999,
        # expSkillGrowCoef=
        # expSkillReduserCoef=
        points=6000,
        x=0,
        y=0,
        # deleteEnqueued=
        # canDelete=
    )

    clan = DB_Clan(
        name='AdminClan',
        shortName='CLAN',
        description='description',
        level=0,
        rating=19000,
        type=1,
        aliance=2,
        race=2,
        enemies=str([]),
        friends=str([]),
        logoFileName='',
    )
    item = DB_Item(ownerId=1, guid="2498jd32nd2",
                    class_number=4,
                    where=1,
                    wear=100,
                    in_using=False)

    angar = DB_Angar(ownerId=1, classNumbers=12)

    skills = DB_Skill()

    player = DB_Player(player=b_player, clan=clan, skills=skills, angar=[angar], items=[item])

    clan.leader = b_player
    clan.members.append(b_player)

    session.add(angar)
    session.add(item)
    session.add(player)
    session.add(clan)
    session.add(b_player)
    session.add(skills)

    session.commit()

def create_player2():
    b_player = DB_B_Player(
        login="login2",
        password="passwd",
        cash=5000000,
        bonus=5000,
        locationId=1,
        experience=468770,
        # clanRequestStatus=
        # clanJoinRequestStatus=
        # PlayerRelation=
        race=2,
        avatar=1001,
        aliance=2,
        rating=50000,
        role=2,
        class_number=2,
        # expSkillGrowCoef=
        # expSkillReduserCoef=
        points=6000,
        x=0,
        y=0,
        # deleteEnqueued=
        # canDelete=
    )
    clan = session.query(DB_Clan).get(1)

    item = DB_Item(ownerId=2, guid="249812jd32nd2",
                    class_number=4,
                    where=1,
                    wear=100,
                    in_using=False)

    angar = DB_Angar(ownerId=2, classNumbers=12)

    skills = DB_Skill()

    player = DB_Player(player=b_player, clan=clan, skills=skills, angar=[angar], items=[item])

    # clan.leader = b_player
    clan.members.append(b_player)

    session.add(angar)
    session.add(item)
    session.add(player)
    session.add(clan)
    session.add(b_player)
    session.add(skills)

    session.commit()


def create_tables():
    Base.metadata.create_all(bind=engine)


def main():
    # pass
    create_tables()
    create_player()
    create_player2()
