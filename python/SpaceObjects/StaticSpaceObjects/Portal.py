from ...BaseClass.StaticSpaceObject import StaticSpaceObject
from python.Static.cfg.StaticSpaceObject.portal import get_to_id

class Portal(StaticSpaceObject):

    def __init__(self, Game, data, LocationClass, count):
        super().__init__(Game, data, LocationClass)
        self.count = count


    def SetPlayer(self, Player):
        to_id = int(str(self.id)[1:])
        to_Location = getattr(self.Game, f'Location_{to_id}')
        self.Portal = getattr(to_Location, f'StaticSpaceObject_4{get_to_id(to_id, self.count)}')
        to_Location.SetPlayer(Player, (self.Portal.x, self.Portal.y))

