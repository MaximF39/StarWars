from python.Static.ResourceStrings import ResourceStrings as Resourcestrs
from python.Static.RaceStrings import RaceStrings as Racestrs


class Race:
    UNDEFINED: str = Resourcestrs.Undefined
    OMOLENIAN_ID: int = 1
    OMOLENIAN: str = Racestrs.Omolenian
    OMOLENIAN_COLOR: int = 16711680
    OMOLENIAN_DARK_COLOR: int = 5570560
    OMOLENIAN_LIGHT_COLOR: int = 16733525
    OMOLENIAN_GRAY_COLOR: int = 9340550
    OMOLENIAN_COLOR_STR: str = "#FF0000"
    IRRIITIAN_ID: int = 2
    IRRIITIAN: str = Racestrs.Irritian
    IRRIITIAN_COLOR: int = 16776960
    IRRIITIAN_DARK_COLOR: int = 5592320
    IRRIITIAN_LIGHT_COLOR: int = 16777045
    IRRIITIAN_GRAY_COLOR: int = 11053212
    IRRIITIAN_COLOR_STR: str = "#FFCC00"
    ANID_ID: int = 3
    ANID: str = Racestrs.Anid
    ANID_COLOR: int = 65280
    ANID_DARK_COLOR: int = 21760
    ANID_LIGHT_COLOR: int = 5635925
    ANID_GRAY_COLOR: int = 11187626
    ANID_COLOR_STR: str = "#00FF00"
    MEDRAMIL_ID: int = 4
    MEDRAMIL: str = Racestrs.Medramill
    MEDRAMIL_COLOR: int = 6206719
    MEDRAMIL_DARK_COLOR: int = 21896
    MEDRAMIL_LIGHT_COLOR: int = 8701439
    MEDRAMIL_GRAY_COLOR: int = 8892627
    MEDRAMIL_COLOR_STR: str = "#0088FF"
    KAANIAN: str = Racestrs.Kraanian
    GULDUC: str = Racestrs.Gulduc
    XENORUIT: str = Racestrs.Xenoruit
    KAANIAN_ID: int = 7
    GULDUC_ID: int = 5
    XENORUIT_ID: int = 6
    KAANIAN_COLOR = 16742144
    KAANIAN_DARK_COLOR: int = 11883520
    GULDUC_COLOR: int = 12359960
    GULDUC_DARK_COLOR: int = 11044885
    XENORUIT_COLOR: int = 11927740
    XENORUIT_DARK_COLOR: int = 5570560
    NEOALIANCE_COLOR: int = 16729088
    MEDAN_COLOR: int = 6206719
    CORSAIRBROTHERHOOD_COLOR = 12359960
    XENOEMPIRE_COLOR = 11927740
    SUPREMECOUNCIL_COLOR: int = 16742144
    FLORIDVORTEX_COLOR: int = 11927740
    NeoAliance: int = 1
    Medan: int = 2
    CorsairBrotherhood: int = 3
    XenoEmpire: int = 4
    SupremeCouncil: int = 5
    FloridVortex: int = 6

    def defineColor(self, param1: str) -> int:
        match param1:
            case self.OMOLENIAN:
                return self.OMOLENIAN_COLOR
            case self.IRRIITIAN:
                return self.IRRIITIAN_COLOR
            case self.ANID:
                return self.ANID_COLOR
            case self.MEDRAMIL:
                return self.MEDRAMIL_COLOR
            case self.KAANIAN:
                return self.KAANIAN_COLOR
            case self.GULDUC:
                return self.GULDUC_COLOR
            case self.XENORUIT:
                return self.XENORUIT_COLOR
            case _:
                return 15658734

    def defineColorById(self, param1: int) -> int:
        match param1:
            case self.OMOLENIAN_ID:
                return self.OMOLENIAN_COLOR
            case self.IRRIITIAN_ID:
                return self.IRRIITIAN_COLOR
            case self.ANID_ID:
                return self.ANID_COLOR
            case self.MEDRAMIL_ID:
                return self.MEDRAMIL_COLOR
            case self.KAANIAN_ID:
                return self.KAANIAN_COLOR
            case self.GULDUC_ID:
                return self.GULDUC_COLOR
            case self.XENORUIT_ID:
                return self.XENORUIT_COLOR
            case _:
                return 15658734

    def defineAlianceColorById(self, param1: int) -> int:
        match param1:
            case self.NeoAliance:
                return self.NEOALIANCE_COLOR
            case self.Medan:
                return self.MEDAN_COLOR
            case self.CorsairBrotherhood:
                return self.CORSAIRBROTHERHOOD_COLOR
            case self.XenoEmpire:
                return self.XENOEMPIRE_COLOR
            case self.SupremeCouncil:
                return self.SUPREMECOUNCIL_COLOR
            case self.FloridVortex:
                return self.FLORIDVORTEX_COLOR
            case _:
                return 15658734

    def defineColorStr(self, param1: str) -> str:
        match param1:
            case self.OMOLENIAN:
                return self.OMOLENIAN_COLOR_STR
            case self.IRRIITIAN:
                return self.IRRIITIAN_COLOR_STR
            case self.ANID:
                return self.ANID_COLOR_STR
            case self.MEDRAMIL:
                return self.MEDRAMIL_COLOR_STR
            case _:
                return "#EEEEEE"

    def defineDarkColor(self, param1: str) -> int:
        match param1:
            case self.OMOLENIAN:
                return self.OMOLENIAN_DARK_COLOR
            case self.IRRIITIAN:
                return self.IRRIITIAN_DARK_COLOR
            case self.ANID:
                return self.ANID_DARK_COLOR
            case self.MEDRAMIL:
                return self.MEDRAMIL_DARK_COLOR
            case self.KAANIAN:
                return self.KAANIAN_DARK_COLOR
            case self.GULDUC:
                return self.GULDUC_DARK_COLOR
            case self.XENORUIT:
                return self.XENORUIT_DARK_COLOR
            case _:
                return 10066329

    def defineLightColorById(self, param1: int) -> int:
        match param1:
            case self.OMOLENIAN_ID:
                return self.OMOLENIAN_LIGHT_COLOR
            case self.IRRIITIAN_ID:
                return self.IRRIITIAN_LIGHT_COLOR
            case self.ANID_ID:
                return self.ANID_LIGHT_COLOR
            case self.MEDRAMIL_ID:
                return self.MEDRAMIL_LIGHT_COLOR
            case _:
                return 16777215

    def defineLightColor(self, param1: str) -> int:
        match param1:
            case self.OMOLENIAN:
                return self.OMOLENIAN_LIGHT_COLOR
            case self.IRRIITIAN:
                return self.IRRIITIAN_LIGHT_COLOR
            case self.ANID:
                return self.ANID_LIGHT_COLOR
            case self.MEDRAMIL:
                return self.MEDRAMIL_LIGHT_COLOR
            case _:
                return 16777215

    def definePluralById(self, param1: int) -> str:
        match param1:
            case self.OMOLENIAN_ID:
                return Racestrs.Omolenians
            case self.IRRIITIAN_ID:
                return Racestrs.Irritians
            case self.ANID_ID:
                return Racestrs.Anids
            case self.MEDRAMIL_ID:
                return Racestrs.Medramills
            case self.GULDUC_ID:
                return Racestrs.Gulducs
            case self.KAANIAN_ID:
                return Racestrs.Kraanians
            case self.XENORUIT_ID:
                return Racestrs.Xenoruits
            case _:
                return self.UNDEFINED

    def defineById(self, param1: int) -> str:
        match param1:
            case self.OMOLENIAN_ID:
                return self.OMOLENIAN
            case self.IRRIITIAN_ID:
                return self.IRRIITIAN
            case self.ANID_ID:
                return self.ANID
            case self.MEDRAMIL_ID:
                return self.MEDRAMIL
            case self.GULDUC_ID:
                return self.GULDUC
            case self.KAANIAN_ID:
                return self.KAANIAN
            case self.XENORUIT_ID:
                return self.XENORUIT
            case _:
                return self.UNDEFINED

    def defineId(self, param1: str) -> int:
        match param1:
            case self.OMOLENIAN:
                return self.OMOLENIAN_ID
            case self.IRRIITIAN:
                return self.IRRIITIAN_ID
            case self.ANID:
                return self.ANID_ID
            case self.MEDRAMIL:
                return self.MEDRAMIL_ID
            case self.XENORUIT:
                return self.XENORUIT_ID
            case self.KAANIAN:
                return self.KAANIAN_ID
            case self.GULDUC:
                return self.GULDUC_ID
            case _:
                return 0

    def defineGrayColor(self, param1: str) -> int:
        match param1:
            case self.OMOLENIAN:
                return self.OMOLENIAN_GRAY_COLOR
            case self.IRRIITIAN:
                return self.IRRIITIAN_GRAY_COLOR
            case self.ANID:
                return self.ANID_GRAY_COLOR
            case self.MEDRAMIL:
                return self.MEDRAMIL_GRAY_COLOR
            case _:
                return 11184810
