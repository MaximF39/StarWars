from python.Base.Event.CashEvent import CashEvent
from python.Static.cfg.cfg_player import get_cost_reset_skills


class SkillsEvent:
    freeSkills: int
    skills: dict
    use_skills: int = 0
    count_reset_skills: int
    level: int

    def __init__(self):
        for k, v in self.skills.items():
            self.use_skills += v
        self.freeSkills = self.use_skills - self.level

    def commitSkills(self, dict_: dict):  # name : append count
        for k, v in dict_.items():
            if self.freeSkills - v >= 0 and self.skills[k] + v < 13:
                self.freeSkills -= v
                self.skills[k] += v

    def reset_skills(self):
        self.count_reset_skills += 1
        for k in self.skills:
            self.skills[k] = 0
        self.freeSkills = self.level

