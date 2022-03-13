from abc import ABC

from python.Game._Component.Event.E_Entity.E_Pvp import Pvp
from python.Static.ParseJson import item_id
from python.Static.Type.T_PlayerSkill import T_PlayerSkill


class SpaceDroid(Pvp, ABC):
    armor: int

    def __init__(self, class_number, Player):
        self.Owner = Player
        self.__dict__.update(item_id(class_number))
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
            T_PlayerSkill.Repairing: 0,
            T_PlayerSkill.Attacking: tactics,
            T_PlayerSkill.Defending: tactics,
            T_PlayerSkill.Targeting: tactics,
        }
