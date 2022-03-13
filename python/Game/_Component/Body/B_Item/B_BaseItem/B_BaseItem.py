import copy
import uuid


class B_BaseItem:

    def __init__(self, Game, data, Owner):
        self.__dict__.update(data)
        self.Owner = Owner
        self.Game = Game
        self.satisfying = self.get_satisfying
        self.guid = self.__get_guid()

    def ItemForPlayer(self, Player):
        Fake = copy.copy(self)
        Fake.new_owner(Player)
        return Fake

    @property
    def wear(self):
        return self.wear

    @staticmethod
    def __get_guid():
         return uuid.uuid4().bytes

    def copy_class(self):
        class_ = copy.copy(self)
        class_.guid = self.__get_guid()
        return class_

    @property
    def get_satisfying(self):
        return True
        if not hasattr(self, "restrictions") or not self.Owner or self.Owner.__name__ == 'DB_Planet':
            return True
        skills = self.Owner.skills
        for skill in self.restrictions:
            match skill[Keys.type]:
                case 2:
                    if skill['value'] > skills[skill['value_type']]:
                        return False
                case 4:
                    if skill['value'] > self.Owner.ship['cpu']:
                        return False
                case 5:
                    if self.Owner.status > skill['value']:  # -3 > -2 пир или коп и ниже тоже
                        return False
                case 6:
                    if self.Owner.status < skill['value']:  # 3 < 2 # player < need -> False
                        return False
                case _:
                    # print('Не понятный тип', skill['type'])
                    pass
            return True

    def get_size(self, count):
        return count * self.size

    def get_cost(self, count):
        return count * self.cost

    @staticmethod
    def _here_type(other, type_):
        if not isinstance(other, type(type_)):
            raise TypeError('Не является классом', type(type_))