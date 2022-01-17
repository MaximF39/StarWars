from python.Static.Type.ShipType import *
from python.Static.Type.Race import Race

weak_system = [2, 9, 6, 8, 5, 43, 30, 46, 105, 106, 107, 108, 109, 120, 114, 115, 125, 111, 112, 113]
medium_system = [7, 38, 1, 4]
strong_system = [68, 69, 70, 71]


def weak_ship(race):
    pref = f'{race - 1}0'

    return [
    int(pref + str(OTransport)),
    # (хз корвет),
    int(pref + str(OIntercepter)),
    int(pref + str(OFregat)),
    int(pref + str(OSience)),
    int(pref + str(OLMiner))
    ]

def medium_ship(race):
    pref = f'{race - 1}0'
    return  [
    int(pref + str(OCruiser)),
    int(pref + str(OLinkor)),
    int(pref + str(OIntercepterHavy)),
    int(pref + str(OFregatArmored)),
    int(pref + str(OFregatAssault)),
    int(pref + str(OFregatAssaultM1)),
    int(pref + str(OScout)),
]

def strong_ship(race):
    pref = f'{race - 1}0'
    return [
    int(pref + str(OBrig)),
    int(pref + str(OPalaven)),
]


