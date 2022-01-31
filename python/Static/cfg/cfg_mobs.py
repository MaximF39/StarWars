from python.Static.Type.ShipType import ShipType
from python.Static.Type.ItemClass import ItemClass
from python.Static.Type.PlayerSkillType import PlayerSkillType
from python.Static.Type.NameSystems import SystemName

r = 1500

mobs_data = {
"max_x": r,
"max_y": r,
"min_x": -r,
"min_y": -r,
}

name = 'strong mob for Astra'
# 1 - weak, 2 - middle, 3 -strong
# 105, 106, 107 - weak(green)
# 6, 8, 38 - middle(green)
# 68 - strong(green)

ship_little = [ShipType.OIntercepter,ShipType.OTransport,ShipType.OSience,ShipType.OIndustrial],
ship_middle = [ShipType.OCruiser,ShipType.OLinkor,ShipType.OFregat,ShipType.OShockBrig,ShipType.OSiegeBrig]
ship_strong = [ShipType.OScout,ShipType.OSiegeLinkor,ShipType.OPalaven]

devices_little = [ItemClass.Battery, ItemClass.Damage, ItemClass.RepairDroid, ItemClass.Turbo, ItemClass.Shield, ItemClass.KEngine]
devices_middle = [*devices_little, ItemClass.Nitrinium,ItemClass.Phaser,ItemClass.Energon,ItemClass.Armor,ItemClass.Absorber,ItemClass.SuperioritySphere,]
devices_strong = [*devices_middle, ItemClass.Reflector,ItemClass.livearmor,ItemClass.MetaController,ItemClass.VacuumCoreBattery,ItemClass.XenoArmor]

ship_weapon = {
    ShipType.OPalaven: [ItemClass.ResinRocket,ItemClass.SplashRocket,ItemClass.SplashRocket, ItemClass.Desintegrator],
    ShipType.OCruiser: [ItemClass.ResinRocket,ItemClass.SplashRocket, ItemClass.MultiBlaster],
    ShipType.OLinkor: [ItemClass.ResinRocket,ItemClass.SplashRocket,ItemClass.MultiBlaster],
    ShipType.OFregat: [ItemClass.ResinRocket,ItemClass.Desintegrator],
    ShipType.OScout: [ItemClass.SplashRocket,ItemClass.Desintegrator],
    ShipType.OShockBrig: [ItemClass.SplashRocket,ItemClass.Desintegrator],
    ShipType.OSiegeBrig: [ItemClass.SplashRocket,ItemClass.Desintegrator],
    ShipType.OSiegeLinkor: [ItemClass.ResinRocket,ItemClass.SplashRocket,ItemClass.Desintegrator,ItemClass.Desintegrator],
    ShipType.OTransport: [ItemClass.AutoGun],
    ShipType.OSience: [ItemClass.Gun],
    ShipType.OIndustrial: [ItemClass.AutoGun],
    ShipType.OIntercepter: [ItemClass.MachineGun, ItemClass.AutoGun]
}

skills_little = [{
    PlayerSkillType.Defending: 0,
    PlayerSkillType.Attacking: 0,
    PlayerSkillType.Targeting: 0,
}]
skills_middle = [{
    PlayerSkillType.Defending: 6,
    PlayerSkillType.Attacking: 6,
    PlayerSkillType.Targeting: 6,
}]
skills_strong = [{
    PlayerSkillType.Defending:12,
    PlayerSkillType.Attacking:12,
    PlayerSkillType.Targeting:12,
}]

Location_mobs = {
    SystemName.neu: [ShipType.OCruiser,ShipType.OCruiser,ShipType.OLinkor],
    SystemName.statu: [ShipType.OCruiser,ShipType.OLinkor,ShipType.OFregat],
    SystemName.skois: [ShipType.OCruiser,ShipType.OLinkor,ShipType.OFregat],
    SystemName.cukita: [ShipType.OPalaven,ShipType.OPalaven],
    SystemName.lerno: [ShipType.OShockBrig,ShipType.OSiegeBrig,ShipType.OSiegeLinkor],
    SystemName.mungo: [ShipType.OShockBrig,ShipType.OSiegeBrig],
    SystemName.diversi: [ShipType.OShockBrig,ShipType.OSiegeBrig],
}