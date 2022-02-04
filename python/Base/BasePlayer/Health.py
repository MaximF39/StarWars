from python.Static.cfg.cfg_player import recovery_health
class Health:

    def __init__(self):
        self.health = self.ship['maxHealth']

    def __get_parameter_repair(self):
        self.__change_health(recovery_health(self.ship['maxHealth'],
                                             self.skills['Repairing']))

    def get_damage_weapon(self, damage):
        self.__change_health(-damage * (self.ship["shields"] / 100))

    def get_damage_device(self, damage):
        self.__change_health(-damage)

    def __change_health(self, health):
        sum_health = self.health + health
        if self.ship['maxHealth'] > sum_health > 0:
            self.health += health
        elif sum_health > self.ship['maxHealth']:
            self.health = self.ship['maxHealth']
        elif 0 > sum_health:
            self.health = 0
            self.dead()
            self.PacMan.shipDestroyed()
            return
        else:
            raise NotImplementedError("error")
        self.PacMan.shipHealth()

    # def dead(self):
    #     raise NotImplementedError("This function dead need to redefine")

    def dead(self):
        self.get_drop()  # send req
