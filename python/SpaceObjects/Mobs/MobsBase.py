from ...Packages.ShipState import ShipState


class Mobs(ShipState):
    class_number: int = 0
    __variable: list = ["player", "mob", "object", ""]

    def __init__(self, dict_: dict):
        self.__toBegin()

        self.device: list = dict_["device"]
        self.weapons: list = dict_["weapons"]
        self.x: float = dict_["x"]
        self.y: float = dict_["y"]
        self.state: float = dict_["state"]
        self.target_x: float = dict_["target_x"]
        self.target_y: float = dict_["target_y"]
        self.object_to_reach_id: int = dict_["object_to_reach_id"]
        self.object_to_reach_type: int = dict_["object_to_reach_type"]
        self.Player_relation: int = dict_["Player_relation"]
        self.id = dict_["id"]
        self.health = dict_["health"]
        self.energy = dict_["energy"]
        self.speed = dict_["speed"]

    def main(self):
        objects = self.requestLocation()
        if not self.__isTaking and not self.__isAttack:
            for obj in objects:
                self.send_dev(obj)
        else:
            if self.object_to_reach_id not in objects:
                self.__toBegin()

    def update(self):
        self.move()

    def move(self):
        pass

    def requestLocation(self):
        # запрос к локации, ответ в переменную response
        response = None
        objects = response.object  # все объекты на локации
        return objects

    def send_dev(self, object=None):
        typeObject: str = self.__examination(object)
        if typeObject == self.__variable[0]:
            self.__attack(object.id)
        elif typeObject == self.__variable[1] and object.class_number != self.class_number:
            self.__attack(object.id)
        elif typeObject == self.__variable[2]:
            self.__take(object.guid)

    def getPlayerDamage(self, id: int, hp: int) -> None:
        self.__setHealth(hp)
        self.__attack(id)

    def getDevice(self) -> list:
        return self.device

    def getWeapons(self) -> list:
        return self.weapons

    def __toBegin(self):
        self.__isTaking: bool = False
        self.__isAttack: bool = False

    def __examination(self, object) -> str:
        if object.id > 0:
            return self.__variable[0]
        elif object.id < 0:
            return self.__variable[1]
        elif object.guid is not None:
            return self.__variable[2]
        else:
            return self.__variable[3]

    def __attack(self, id: int):
        self.__isTaking = False
        self.__isAttack = True
        self.object_to_reach_id = id
        pass

    def __take(self, guid: int):
        self.__isTaking = True
        self.object_to_reach_id = guid
        pass

    def __setHealth(self, health: int):
        self.health -= health

    def __setEnergy(self, energy: int):
        self.energy -= energy
