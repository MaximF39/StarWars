# from ..Utils.Vector2D import Vector2D

class SpaceObject:
    id: int
    type: int
    size: int
    race: str
    aliance: int

    def __init__(self, StarWars, data):
        super().__init__()
        self.Game = StarWars
        self.id = data['id']
        self.type = data['Types'] if 'Types' in data else None
        self.size = data['size'] if 'size' in data else 10000
        self.race = data['race']
        self.aliance = data['aliance']

    def set_space_object_on_location(self, id_location):
        getattr(self.Game, f"Location_{id_location}").set_object_space(self.__dict__, self.type)

    # def createSelection(self, param1: uint, param2: int):
    #     _loc3_: = None
    #     _loc4_: Shape = None
    #     _loc5_: Shape = None
    #     _loc6_: Shape = None
    #     _loc3_ = None
    #     _loc4_ = None
    #     _loc5_ = None
    #     _loc6_ = None
    #     _loc3_ = ()
    #     _loc3_.mouseEnabled = False
    #     _loc3_.mouseChildren = False
    #     (_loc4_ =  Shape()).graphics.beginFill(param1)
    #     _loc4_.graphics.drawRect(0, 0, param2 / 3, param2 / 3)
    #     _loc4_.graphics.drawRect(0, param2 / 3 * 2, param2 / 3, param2 / 3)
    #     _loc4_.graphics.drawRect(param2 / 3 * 2, 0, param2 / 3, param2 / 3)
    #     _loc4_.graphics.drawRect(param2 / 3 * 2, param2 / 3 * 2, param2 / 3, param2 / 3)
    #     _loc4_.x = _loc4_.width / -2
    #     _loc4_.y = _loc4_.height / -2
    #     _loc3_.addChild(_loc4_)
    #     (_loc5_ =  Shape()).graphics.lineStyle(2, param1, 1)
    #     _loc5_.graphics.drawEllipse(0, 0, param2, param2)
    #     _loc5_.x = _loc5_.width / -2
    #     _loc5_.y = _loc5_.height / -2
    #     _loc5_.mask = _loc4_
    #     _loc3_.addChild(_loc5_)
    #     (_loc6_ =  Shape()).graphics.lineStyle(0, 0, 0)
    #     _loc6_.graphics.beginFill(16777215, 0.2)
    #     _loc6_.graphics.drawEllipse(0, 0, param2, param2)
    #     _loc6_.x = _loc5_.width / -2
    #     _loc6_.y = _loc5_.height / -2
    #     _loc3_.addChild(_loc6_)
    #     _loc3_.cacheAsBitmap = True
    #     return _loc3_
    #
    # def initialize(self) -> None:
    #     super.initialize()
    #     doubleClickEnabled = True
    #     if self.allowSelection:
    #         self._sSelection = createSelection(self.selectionColor, self.displaySize * 1.3)
    #         self._sHoverSelection = createSelection(self.selectionColor, self.displaySize * 1.3)
    #         self.initEvents()
    #     image.x = image.width / -2
    #     image.y = image.height / -2
    #
    # def initEvents(self) -> None:
    #     addEventListener(MouseEvent.ROLL_OVER, self.onRollOver)
    #     addEventListener(MouseEvent.ROLL_OUT, self.onRollOut)
    #     addEventListener(MouseEvent.CLICK, self.onMouseClick)
    #     addEventListener(MouseEvent.DOUBLE_CLICK, self.onMouseDoubleClick)
    #
    # def uninitEvents(self) -> None:
    #     removeEventListener(MouseEvent.ROLL_OVER, self.onRollOver)
    #     removeEventListener(MouseEvent.ROLL_OUT, self.onRollOut)
    #     removeEventListener(MouseEvent.CLICK, self.onMouseClick)
    #     removeEventListener(MouseEvent.DOUBLE_CLICK, self.onMouseDoubleClick)
    #
    # def uninitialize(self) -> None:
    #     self.uninitEvents()
    #     self.hideHoverSelection()
    #     self.removeSelection()
    #     self._sHoverSelection = None
    #     self._sSelection = None
    #     super.uninitialize()
    #
    # def onMouseClick(self, param1: MouseEvent) -> None:
    #     if param1.eventPhase != EventPhase.AT_TARGET:
    #         return
    #     if parent != Space:
    #         return
    #     _loc2_: int = self.getTimer()
    #     if _loc2_ - self._iLastClicked < Config.doubleClickDelay:
    #         self.onMouseDoubleClick(param1)
    #     else:
    #         # GameEngine.selected = self
    #         pass
    #     self._iLastClicked = _loc2_
    #     param1.stopPropagation()
    #
    # def onMouseDoubleClick(self, param1: None) -> None:  # MouseEvent
    #     if param1.eventPhase != EventPhase.AT_TARGET:
    #         return
    #     if parent != Space:
    #         return
    #     param1.stopPropagation()
    #     GameEngine.selected = self
    #     GameEngine.setObjectToReach()
    #     GameEngine.setObjectToAttack()
    #
    # def removeSelection(self) -> None:
    #     if self._sSelection != None and contains(self._sSelection):
    #         removeChild(self._sSelection)
    #
    # def addSelection(self) -> None:
    #     if self._sSelection == None or contains(self._sSelection):
    #         return
    #     self._sSelection.alpha = 1
    #     addChildAt(self._sSelection, 0)
    #
    # def onRollOver(self, param1) -> None:  # : MouseEvent
    #     self.showHoverSelection()
    #     param1.stopPropagation()
    #
    # def onRollOut(self, param1) -> None:  #: MouseEvent
    #     self.hideHoverSelection()
    #     param1.stopPropagation()
    #
    # def showHoverSelection(self) -> None:
    #     if self._sHoverSelection == None or contains(self._sHoverSelection):
    #         return
    #     self._sHoverSelection.alpha = 0.5
    #     addChildAt(self._sHoverSelection, 0)
    #     self.hoverSelectionHeight()
    #     return self._sHoverSelection.height
    #
    # def hideHoverSelection(self) -> None:
    #     if self._sHoverSelection == None or not contains(self._sHoverSelection):
    #         return
    #     removeChild(self._sHoverSelection)
    #
    # def distanceTo(self, param1: SpaceObject) -> float:
    #     if None == param1:
    #         return 0
    #     return Vector2D.calculateLength(x - param1.x, y - param1.y)
    #
    # def weight(self) -> int:
    #     return self.size
    #
    # def cost(self) -> int:
    #     return self._iCost
    #
    # def cost(self, param1: int) -> None:
    #     self._iCost = param1
    #     self.perimeter(): int
    #     return self.image.width * self.image.height
    #
    #     typeOfLocation(): int
    #
    # if self is Ship:
    #     return ShipLocationType.SHIP
    #
    # if self is Planet:
    #     return ShipLocationType.PLANET
    #
    # return 0
    #
    #
    # displaySize() -> float:
    #
    # if self._nDisplaySize == 0:
    #     self._nDisplaySize = math.max(image.width, image.height)
    #
    # return self._nDisplaySize
    #
    # isInView() -> bool:
    #
    # return Space.isInView(self)
    #
    # def calculateScale(self) -> None:
    #     self._nScale = math.sqrt(self.DEF_SPACE_OBJECT_PERIMERER / self.perimeter)
    #     image.scaleX = self._nScale
    #     image.scaleY = self._nScale
    #     self._nScale = math.sqrt(size) * Space.scale / 250 * self._nClassScale
    #     scaleX = self._nScale
    #     scaleY = self._nScale
    #
    # def update(self) -> None:
    #     def playSound(self, param1: Sound, param2: float = 1.0) -> None:
    #         SoundEffects.playSpaceSound(param1, x, y, param2)
