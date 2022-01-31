from python.Static.Type.ShipType import ShipType
# O, I, A, M
races = ['', '10', '20', '30']

_def = [
    {ShipType.OIntercepter: ShipType.OIntercepterHavy},
        {ShipType.OTransport: ShipType.OLRTransport},
        {ShipType.OFregat: ShipType.OFregatArmored},
        {ShipType.OIndustrial: ShipType.OScout}, # в будущем
        {ShipType.OScout: ShipType.OSience},
        {ShipType.OLinkor: ShipType.OSiegeLinkor},
        {ShipType.OIntercepterHavy: ShipType.OIntercepterCorsar},
        {ShipType.OIntercepterCorsar: ShipType.PIntercepterCorsar},
        {ShipType.OFregatArmored: ShipType.OFregatAssault},
        {ShipType.OFregatAssault: ShipType.OFregatAssaultM1},
        {ShipType.OCarrier: ShipType.OBrig}, # в будущем
        {ShipType.OBrig: ShipType.OShockBrig},
        {ShipType.OShockBrig: ShipType.OSiegeBrig},
        {ShipType.OLRTransport: ShipType.OFTransport},]

cfg_upgrade ={}

for race in races:
    for dict_ in _def:
        for k, v in dict_.items():
            if v == 8001:
                to_ship = v
            else:
                to_ship = int(f'{race}{v}')
            cfg_upgrade[int(f'{race}{k}')] = to_ship

if __name__ == '__main__':
    print(cfg_upgrade)


