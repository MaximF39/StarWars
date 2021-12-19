from ItemClass import ItemClass
# from ResourceLoader import ResourceLoader
class ResourceManager:
    _aParameters: list

    # def loadParameters(self, param1: list) -> None:
    #     _loc2_: int = 0
    #     _loc3_: None = None # ResourceParameters
    #     _aParameters = param1
    #     _loc4_: list = getClasses()
    #     for each(_loc2_ in _loc4_):
    #         _loc3_ = findParameters(_loc2_)
    #         if (_loc3_ == None):
    #             throw
    #             Error(Resourcestrs.NoParametersForWeapon + " " + _loc2_.tostr())

    def Classes(self) -> list:
        _loc1_: list = list()
        _loc1_.append(ItemClass.Iron)
        _loc1_.append(ItemClass.IronOre)
        _loc1_.append(ItemClass.Gold)
        _loc1_.append(ItemClass.GoldOre)
        _loc1_.append(ItemClass.Titan)
        _loc1_.append(ItemClass.TitanOre)
        _loc1_.append(ItemClass.Osmium)
        _loc1_.append(ItemClass.OsmiumOre)
        return _loc1_


    # def findParameters(self, param1: int) -> None: # ResourceParameters
    #     _loc2_: ResourceParameters = None
    #     for each(_loc2_ in _aParameters):
    #         if (_loc2_.classfloat == param1):
    #             return _loc2_
    #     return None

    def BitmapName(self, param1: int) -> str:
        match param1:
            case ItemClass.Iron:
                return "Iron"
            case ItemClass.IronOre:
                return "IronOre"
            case ItemClass.Titan:
                return "Titan"
            case ItemClass.TitanOre:
                return "TitanOre"
            case ItemClass.Gold:
                return "Gold"
            case ItemClass.GoldOre:
                return "GoldOre"
            case ItemClass.Osmium:
                return "Osmium"
            case ItemClass.OsmiumOre:
                return "OsmiumOre"
            case ItemClass.Minerals:
                return "Minerals"
            case ItemClass.Organic:
                return "Organic"
            case ItemClass.XenoCrystall:
                return "XenoCrystall"
            case ItemClass.OTrash:
                return "OTrash"
            case ItemClass.ITrash:
                return "ITrash"
            case ItemClass.ATrash:
                return "ATrash"
            case ItemClass.MTrash:
                return "MTrash"
            case ItemClass.GTrash:
                return "GTrash"
            case ItemClass.XTrash:
                return "XTrash"
            case ItemClass.KTrash:
                return "KTrash"
            case ItemClass.Catalyst:
                return "Catalyst"
            case ItemClass.unknowTrash:
                return "unknowTrash"
            case ItemClass.xMedal1:
                return "xMedal1"
            case ItemClass.microscheme:
                return "microscheme"
            case _:
                return "XTrash"

    # def BitmapByClass(self, param1: int) -> Bitmap:
    #     return getBitmap(getBitmapName(param1))

    # def Bitmap(self, param1: str): # Bitmap
    #     return ResourceLoader.getResource(ResourceLoader.RESOURCES, param1)



