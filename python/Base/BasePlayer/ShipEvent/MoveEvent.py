from python.Static.Type.ObjectToReachType import ObjectToReachType
from python.Utils.ThreadBase import ThreadBase
from python.Utils.Vector2D import Vector2D
from python.Base.SpaceObject.MovableSpaceObject import MovableSpaceObject


class MoveEvent(MovableSpaceObject, ThreadBase):

    def __init__(self, Game, data):
        MovableSpaceObject.__init__(self, Game, data)
        # self.speed = self.ship['maxSpeed']
        self.targetX = self.x
        self.targetY = self.y

    def WaitForCord(self):
        self.OldTarget = False
        if self.ObjectToReach:
            self.ObjectToReach.set_player(self)
            self.ObjectToReach = False
        else:
            self._set_x_y(self.targetX, self.targetY)

    def _move_coord(self, player_vector, target_vector, targetX, targetY, Location):
        self._set_target_x_y(targetX, targetY)
        if not Location:
            self.ObjectToReach = None
        if self.OldTarget:  # move to move
            self._default_move('move_to_move', player_vector, target_vector)
        else:  # stop to move
            self._default_move('stop_to_move', player_vector, target_vector)
        self.OldTarget = True

    def _default_move(self, mod, player_vector, target_vector):
        if mod == 'move_to_move' or mod == 'stop':
            self.del_thread_timer(self.WaitForCord)
            Vector = player_vector.move(target_vector, self.tick())
            self._set_x_y(Vector2d=Vector)
        else:
            self.tick()
        if mod == 'stop':
            self.not_target()
        else:
            self.targetX = target_vector.x
            self.targetY = target_vector.y
            time_w = player_vector.time_wait(Vector2D(self.targetX, self.targetY))
            self.start_timer_update(self.WaitForCord, time_w)

    def _move_space_object(self, player_vector, target_vector, SpaceObject):
        self.ObjectToReach = SpaceObject
        self.targetX = SpaceObject.x
        self.targetY = SpaceObject.y
        if self.OldTarget:  # move to move
            self._default_move('move_to_move', player_vector, target_vector)
        else:  # stop to move
            self._default_move('stop_to_move', player_vector, target_vector)
        self.OldTarget = True

    def _stop(self, player_vector, target_vector):
        if self.OldTarget:
            self._default_move('stop', player_vector, target_vector)
            self.OldTarget = False

    def move(self, targetX=None, targetY=None, *, stop=False, SpaceObject=None, Location=None):
        player_vector = Vector2D(self.x, self.y, self.speed)
        target_vector = Vector2D(self.targetX, self.targetY)

        if targetX and targetY:
            self._move_coord(player_vector, target_vector, targetX, targetY, Location)
        elif stop:
            self._stop(player_vector, target_vector)
        elif SpaceObject:
            self._move_space_object(player_vector, target_vector, SpaceObject)
        else:
            raise NotImplementedError(f"{targetX=},{targetY=},{SpaceObject=},{stop=}")

        # if SpaceObjectItems:
        #     self.ObjectToReach = SpaceObjectItems
        #     self.targetX = SpaceObjectItems.x
        #     self.targetY = SpaceObjectItems.y
        # else:
        #     if targetX and targetY:
        #         self.targetX = targetX
        #         self.targetY = targetY
        #         if not Location:
        #             self.ObjectToReach = False
        # player_vector = Vector2D(self.x, self.y, self.speed)
        # target_vector = Vector2D(self.targetX, self.targetY)
        # if stop:  # just stop
        #     if self.OldTarget:
        #         self._default_move('stop', player_vector, target_vector)
        #         self.OldTarget = False
        # elif self.OldTarget:  # move to move
        #     self._default_move('move_to_move', player_vector, target_vector)
        #     self.OldTarget = True
        # else:  # stop to move
        #     self._default_move('stop_to_move', player_vector, target_vector)
        #     self.OldTarget = True

    def not_target(self):
        self.targetX = self.x
        self.targetY = self.y

    def _set_x_y(self, x=None, y=None, Vector2d=None):
        if not (x is None and y is None):
            self.x = x
            self.y = y
        elif Vector2d:
            self.x = Vector2d.x
            self.y = Vector2d.y
        else:
            raise NotImplementedError('Not x, y OR Vector2d')

    def _set_target_x_y(self, targetX=None, targetY=None, Vector2d=None):
        if not ((targetX and targetY) or Vector2d):
            raise NotImplementedError('Not targetX, targetY OR Vector2d')
        if targetX and targetY:
            self.targetX = targetX
            self.targetY = targetY
        else:
            self.x = Vector2d.x
            self.y = Vector2d.y

    def set_object_to_reach(self, data):
        match data['type']:
            case ObjectToReachType.PLANET:
                self.move(SpaceObject=getattr(self.Location, f'Planet_{data["id"]}'))
            case ObjectToReachType.SHIP:
                pass
            case ObjectToReachType.BATTLE:
                pass
            case ObjectToReachType.ITEM:
                for item_ in self.Location.inventory:
                    if item_.guid == data['id']:
                        self.move(SpaceObject=item_)
            case ObjectToReachType.STATIC_SPACE_OBJECT:
                self.move(SpaceObject=getattr(self.Location, f'StaticSpaceObject_{data["id"]}'))
            case ObjectToReachType.ASTEROID:
                for Aster in self.SpaceObject.asteroids:
                    if Aster.id == data['id']:
                        self.move(SpaceObject=Aster)
