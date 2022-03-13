from python.Static.Type.Keys import Keys
from python.Static.Type.T_ObjectToReach import T_ObjectToReach
from python.Game._Component.Utils.MyTime import MyTime
from python.Game._Component.Utils.ThreadBase import ThreadBase
from python.Game._Component.Utils.Vector2D import Vector2D
from python.Game._Component.Body.B_SpaceObject.SpaceObject.MovableSpaceObject import MovableSpaceObject


class E_Move(MovableSpaceObject, ThreadBase, MyTime):

    def __init__(self, Game, data):
        MovableSpaceObject.__init__(self, Game, data)
        # self.speed = self.ship[Keys.class_number]
        self.targetX = self.x
        self.targetY = self.y

    def WaitForCord(self):
        self.OldTarget = False
        if self.ObjectToReach:
            self.set_space_object(self.ObjectToReach)
            self.ObjectToReach = None
        else:
            self.set_x_y(self.targetX, self.targetY)

    def _move_coord(self, player_vector, target_vector, targetX, targetY, Location):
        self._set_target_x_y(targetX, targetY)
        if self.OldTarget:  # move to move
            self._default_move('move_to_move', player_vector, target_vector)
        else:  # stop to move
            self._default_move('stop_to_move', player_vector, target_vector)
        self.OldTarget = True

    def _default_move(self, mod, player_vector, target_vector):
        if (mod == 'move_to_move' or mod == 'stop') and self.OldTarget:
            self.del_thread_timer(self.WaitForCord)
            self.OldTick = self.tick()
            Vector = player_vector.move(target_vector, self.OldTick)
            self.x = Vector.x
            self.y = Vector.y
        else:
            self.tick()
        if mod == 'stop':
            self.not_target()
        else:
            self.targetX = target_vector.x
            self.targetY = target_vector.y
            time_w = player_vector.time_wait(Vector2D(self.targetX, self.targetY))
            self.start_timer_update(self.WaitForCord, time_w)
            print(f'{time_w=}, {self.targetX=}, {self.targetY=}')


    def _move_space_object(self, player_vector, target_vector, SpaceObject):
        self.ObjectToReach = SpaceObject
        self._set_target_x_y(SpaceObject.x, SpaceObject.y)
        if self.OldTarget:  # move to move
            self._default_move('move_to_move', player_vector, target_vector)
        else:  # stop to move
            self._default_move('stop_to_move', player_vector, target_vector)
        self.OldTarget = True

    def _stop(self, player_vector, target_vector):
        if self.OldTarget:
            self._default_move('stop', player_vector, target_vector)
            self.OldTarget = False

    def move(self, targetX=None, targetY=None, *, stop=None, SpaceObject=None):
        if (targetX is None or targetY is None) and SpaceObject is None  and stop is None:
            raise NotImplementedError(f"{targetX=}, {targetY=}, {stop=}, {SpaceObject=}")
        if SpaceObject:
            self.ObjectToReach = SpaceObject
            self.targetX = SpaceObject.x
            self.targetY = SpaceObject.y
        else:
            if targetX and targetY:
                self.targetX = targetX
                self.targetY = targetY
        player_vector = Vector2D(self.x, self.y, self.speed)
        target_vector = Vector2D(self.targetX, self.targetY)
        if stop:  # just stop
            if self.OldTarget:
                self._default_move('stop', player_vector, target_vector)
                self.OldTarget = False
        elif self.OldTarget:  # move to move
            self._default_move('move_to_move', player_vector, target_vector)
            self.OldTarget = True
        else:  # stop to move
            self._default_move('stop_to_move', player_vector, target_vector)
            self.OldTarget = True


    def not_target(self):
        self.targetX = self.x
        self.targetY = self.y

    def set_x_y(self, x=None, y=None, Vector2d=None):
        if not (x is None and y is None):
            self.x = x
            self.y = y
        elif Vector2d:
            self.x = Vector2d.x
            self.y = Vector2d.y
        else:
            raise NotImplementedError('Not x, y OR Vector2d')
        self.not_target()

    def _set_target_x_y(self, targetX=None, targetY=None, Vector2d=None):
        if targetX and targetY:
            print(f"{self.targetX=}, {self.targetY=}")
            self.targetX = targetX
            self.targetY = targetY
        elif Vector2d:
            self.x = Vector2d.x
            self.y = Vector2d.y
        else:
            raise NotImplementedError('error')

    def set_object_to_reach(self, data):
        match data[Keys.type]:
            case T_ObjectToReach.PLANET:
                self.move(SpaceObject=getattr(self.Location, f'Planet_{data[Keys.id]}'))
            case T_ObjectToReach.SHIP:
                pass
            case T_ObjectToReach.BATTLE:
                pass
            case T_ObjectToReach.ITEM:
                for item_ in self.Location.inventory:
                    if item_.guid == data[Keys.id]:
                        self.move(SpaceObject=item_)
            case T_ObjectToReach.STATIC_SPACE_OBJECT:
                self.move(SpaceObject=getattr(self.Location, f'StaticSpaceObject_{data[Keys.id]}'))
            case T_ObjectToReach.ASTEROID:
                for Aster in self.SpaceObject.asteroids:
                    if Aster.id == data[Keys.id]:
                        self.move(SpaceObject=Aster)

