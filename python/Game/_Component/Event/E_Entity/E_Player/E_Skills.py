
class E_Skills:
    freeSkills: int
    skills: dict
    use_skills: int = 0
    count_reset_skills: int
    level: int

    def __init__(self):
        for v in self.skills.values():
            self.use_skills += v
        self.freeSkills = self.level - self.use_skills

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

    def add_skills(self):
        self.freeSkills += 1


