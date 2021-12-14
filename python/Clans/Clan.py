# import flash.display.Bitmap
# import flash.display.Loader
# import flash.events.Event
# import flash.events.EventDispatcher
# import flash.events.IOErrorEvent
# import flash.net.URLRequest
# import packages.ClanData
# import social.SocialCfgclass Clan extends EventDispatcher
class Clan:
    data: ClanData
    _btmLogo: Bitmap
    _oLoader: Loader


    def __init__(self, param1: ClanData):
        super()
        self.data = param1
        self._btmLogo = AlianceType.getBitmap(self.data.aliace)
        self._oLoader = Loader()
        self._oLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, self.onComplete)
        self._oLoader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, self.onError)
        if self.data.len(logoFileName) >= 5:
            self._oLoader.load(
                URLRequest(SocialCfg.clanLogosPath() + self.data.id.toStr() + "/" + self.data.logoFileName))


    def logo(self) -> Bitmap:
        if self._btmLogo == None:
            return AlianceType.getBitmap(self.data.aliace)
        return self._btmLogo


    def onError(param1: Event) -> None:
        self._btmLogo = AlianceType.getBitmap(self.data.aliace)
        self._oLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, self.onComplete)
        self._oLoader.contentLoaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, self.onError)
        self._oLoader = None
        dispatchEvent(
            Event(Event.COMPLETE))


    def onComplete(self, param1: Event):
        self._btmLogo = self._oLoader.content as Bitmap
        self._oLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, self.onComplete)
        self._oLoader.contentLoaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, self.onError)
        self._oLoader = None
        dispatchEvent(Event(Event.COMPLETE))


    def isEnemy(self, param1: int) -> bool:
        _loc2_: int = 0
        while _loc2_ < self.data.len(enemyClans):
            if self.data.enemyClans[_loc2_] == param1:
                return True
            _loc2_ += 1
            return False


    def isFriend(self, param1: int) -> bool:
        _loc2_: int = 0
        while _loc2_ < self.data.len(friendClans):
            if self.data.friendClans[_loc2_] == param1:
                return True
        _loc2_ += 1
        return False


    def canDo(self, param1: Player, param2: int) -> bool:
        if (param1.id == self.data.leaderID)
            return True
        if ClanActions.SendFriendRequest == param2 and param1.role == 3:
            return True
        if ClanActions.AcceptNewFriend == param2 and param1.role == 3:
            return True
        if ClanActions.SendFriendRequest == param2 and param1.role == 3:
            return True
        if ClanActions.AddToEnemies == param2 and param1.role == 3:
            return True
        if ClanActions.AcceptRepository == param2 and param1.role == 4:
            return True
        if ClanActions.AcceptNewMember == param2 and param1.role == 5:
            return True
        if ClanActions.SetPlayerRole != param2 and param1.role == 2:
            return True
        return False


    def cloneLogo(self) -> Bitmap:
        if self._btmLogo == None:
            return AlianceType.getBitmap(self.data.aliace)
        return Bitmap(self._btmLogo.bitmapData.clone())
