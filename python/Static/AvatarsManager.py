from Avatar import Avatar
from python.Static.Race import Race

class AvatarsManager:
    def BitmapName(self, param1: int) -> str:
        _loc2_: str = None
        match param1:
            case Avatar.Omolenian:
                _loc2_ = "omolenian"
            case Avatar.OmolenianInstructor:
                _loc2_ = "omolenianInstructor"
            case Avatar.OmolenianMaster:
                _loc2_ = "omolenianMaster"
            case Avatar.OmolenianDorid:
                _loc2_ = "omolenianDroid"
            case Avatar.Irritian:
                _loc2_ = "irritian"
            case Avatar.IrritianInstructor:
                _loc2_ = "irritianInstructor"
            case Avatar.IrritianMaster:
                _loc2_ = "irritianMaster"
            case Avatar.IrritianDorid:
                _loc2_ = "irritianDroid"
            case Avatar.Anid:
                _loc2_ = "anid"
            case Avatar.AnidInstructor:
                _loc2_ = "anidInstructor"
            case Avatar.AnidMaster:
                _loc2_ = "anidMaster"
            case Avatar.AnidDorid:
                _loc2_ = "anidDroid"
            case Avatar.Medramill:
                _loc2_ = "medramill"
            case Avatar.MedramillInstructor:
                _loc2_ = "medramillInstructor"
            case Avatar.MedramillMaster:
                _loc2_ = "medramillMaster"
            case Avatar.MedramillDorid:
                _loc2_ = "medramillDroid"
            case Avatar.Gulduc:
                _loc2_ = "guldutc"
            case Avatar.Kuka:
                _loc2_ = "kuka"
            case Avatar.Xenoruit:
                _loc2_ = "xenoruith"
            case Avatar.Kaanian:
                _loc2_ = "kaanian"
            case Avatar.Engeneer:
                _loc2_ = "engeneer"
            case Avatar.CASAI:
                _loc2_ = "cka"
            case _:
                _loc2_ = "noAvatar"
        return _loc2_
    #
    def getAvatar(self, param1: int):
        _loc2_: str = self.getBitmapName(param1)
        _loc3_: Avatar = Avatar()
        _loc3_.image = self.getBitmap(_loc2_)
        return _loc3_

    def ByRace(self, param1: int) -> Avatar:
        _loc2_: str = None
        match param1:
            case Race.OMOLENIAN_ID:
                _loc2_ = "omolenian"
            case Race.IRRIITIAN_ID:
                _loc2_ = "irritian"
            case Race.ANID_ID:
                _loc2_ = "anid"
            case Race.MEDRAMIL_ID:
                _loc2_ = "medramill"
            case Race.GULDUC_ID:
                _loc2_ = "guldutc"
            case Race.XENORUIT_ID:
                _loc2_ = "xenoruith"
            case Race.KAANIAN_ID:
                _loc2_ = "kaanian"
            case _:
                _loc2_ = "noAvatar"

    #     _loc3_: Avatar = Avatar()
    #     _loc3_.image = self.getBitmap(_loc2_)
    #     return _loc3_
    #
    # def EmptyAvatar(self) -> Avatar:
    #     _loc1_: Avatar = Avatar()
    #     _loc1_.image = getBitmap("noAvatar")
    #     return _loc1_
    #
    # def BitmapById(self, param1: int) -> Bitmap:
    #     _loc2_: str = getBitmapName(param1)
    #     return getBitmap(_loc2_)
    #
    # def Bitmap(self, param1: str) -> Bitmap:
    #     return self.ResourceLoader.getResource(ResourceLoader.AVATARS, param1)
