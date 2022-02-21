from abc import ABC

from python.Base.BasePlayer.Pvp import Pvp
from python.Static.ParseJson import item_id
from python.Static.Type.PlayerSkillType import PlayerSkillType


class SpaceDroid(Pvp, ABC):
    armor: int

    def __init__(self, classNumber, Player):
        self.Owner = Player
        self.__dict__.update(item_id(classNumber))
        data_skills = self.get_data_skills(Player.skills['Tactics'])
        Pvp.__init__(self, self.health, self.Owner.energy, self.armor, data_skills)

    @property
    def x(self):
        return self.Owner.x

    @property
    def y(self):
        return self.Owner.y

    @property
    def energy(self):
        return self.Owner.energy

    @staticmethod
    def get_data_skills(tactics):
        return {
            PlayerSkillType.Repairing: 0,
            PlayerSkillType.Attacking: tactics,
            PlayerSkillType.Defending: tactics,
            PlayerSkillType.Targeting: tactics,
        }
