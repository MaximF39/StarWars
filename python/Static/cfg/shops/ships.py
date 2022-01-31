from python.Static.Type.ShipType import ShipType
from python.Static.Type.Race import Race

weak_system = [2, 9, 6, 8, 5, 43, 30, 46, 105, 106, 107, 108, 109, 120, 114, 115, 125, 111, 112, 113]
medium_system = [7, 38, 1, 4]
strong_system = [68, 69, 70, 71]


def weak_ship(race):
    pref = f'{race - 1}0'
    return [
    int(pref + str(ShipType.OTransport)),
    # (хз корвет),
    int(pref + str(ShipType.OIntercepter)),
    int(pref + str(ShipType.OFregat)),
    int(pref + str(ShipType.OSience)),
    int(pref + str(ShipType.OLMiner))
    ]

def medium_ship(race):
    pref = f'{race - 1}0'
    return  [
    int(pref + str(ShipType.OCruiser)),
    int(pref + str(ShipType.OLinkor)),
    int(pref + str(ShipType.OIntercepterHavy)),
    int(pref + str(ShipType.OFregatArmored)),
    int(pref + str(ShipType.OFregatAssault)),
    int(pref + str(ShipType.OFregatAssaultM1)),
    int(pref + str(ShipType.OScout)),
]

def strong_ship(race):
    pref = f'{race - 1}0'
    return [
    int(pref + str(ShipType.OBrig)),
    int(pref + str(ShipType.OPalaven)),
]


