import sqlalchemy as db
from python.Database.DB_Table.engine import Base

association = db.Table(
    'association', Base.metadata,
    db.Column('player_id', db.Integer, db.ForeignKey('db_b_players.id')),
    db.Column('clan_id', db.Integer, db.ForeignKey('db_clans.id')),
)