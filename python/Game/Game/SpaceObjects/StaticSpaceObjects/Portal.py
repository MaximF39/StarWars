from python.Game._Component.Body.B_SpaceObject.SpaceObject.StaticSpaceObject import StaticSpaceObject
from python.Config.CFG_StaticSpaceObject.portal import get_to_id

class Portal(StaticSpaceObject):

    def __init__(self, Game, data, LocationClass, count):
        StaticSpaceObject.__init__(self, Game, data, LocationClass)
        self.count = count

    def _set_player(self, Player):
        to_id = int(str(self.id)[1:])
        to_Location = getattr(self.Game, f'Location_{to_id}')
        self.Portal = getattr(to_Location, f'StaticSpaceObject_4{get_to_id(to_id, self.count)}')
        to_Location._set_player(Player, (self.Portal.x, self.Portal.y))

