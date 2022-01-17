from python.SpaceObjects.Item import item
from python.Static.Type.ItemClass import ItemClass
from python.Static.Type.Race import Race


def get_inventory(race):
    match race:
        case Race.OMOLENIAN_ID:
            # for i in red_shop:
                # item(i)
            return red_shop
        case Race.IRRIITIAN_ID:
            return yellow_shop
        case Race.ANID_ID:
            return green_shop
        case Race.MEDRAMIL_ID:
            return blue_shop
        case _:
            raise 'Error'
green_shop = []
green_shop.append(item(ItemClass.AnidRezak))
green_shop.append(item(ItemClass.AnidUnzipper))
green_shop.append(item(ItemClass.Turbo))
green_shop.append(item(ItemClass.Processor))
green_shop.append(item(ItemClass.Nitrinium))
green_shop.append(item(ItemClass.AnidEngine))
green_shop.append(item(ItemClass.AnidEngine2))
green_shop.append(item(ItemClass.AnidMiner))
green_shop.append(item(ItemClass.AnidInfantry))
green_shop.append(item(ItemClass.AnidArmored))
green_shop.append(item(ItemClass.ATrash))

blue_shop = []
blue_shop.append(item(ItemClass.LaserGun)) 
blue_shop.append(item(ItemClass.Battery))
blue_shop.append(item(ItemClass.MedramillUnzipper))
blue_shop.append(item(ItemClass.Shield)) 
blue_shop.append(item(ItemClass.Energon)) 
blue_shop.append(item(ItemClass.MAntiFazer))
blue_shop.append(item(ItemClass.RepairDroid)) 
blue_shop.append(item(ItemClass.MRepair2))
blue_shop.append(item(ItemClass.MedramillEngine))
blue_shop.append(item(ItemClass.MedramillEngine2)) 
blue_shop.append(item(ItemClass.MedramilMiner))
blue_shop.append(item(ItemClass.MedramillInfantry)) 
blue_shop.append(item(ItemClass.MedramillArmored))
blue_shop.append(item(ItemClass.MTrash))

red_shop = []
red_shop.append(item(ItemClass.OmolenianRezak)) 
red_shop.append(item(ItemClass.OmolenianUnzipper))
red_shop.append(item(ItemClass.Generator)) 
red_shop.append(item(ItemClass.Damage))
red_shop.append(item(ItemClass.Armor)) 
red_shop.append(item(ItemClass.Phaser))
red_shop.append(item(ItemClass.OmolenianEngine)) 
red_shop.append(item(ItemClass.OmolenianEngine2))
red_shop.append(item(ItemClass.OmolenianEngine3)) 
red_shop.append(item(ItemClass.OmolenianMiner))
red_shop.append(item(ItemClass.OmolenianInfantry))
red_shop.append(item(ItemClass.OmolenianArmored)) 
red_shop.append(item(ItemClass.OTrash))

yellow_shop = []
yellow_shop.append(item(ItemClass.Jalo)) 
yellow_shop.append(item(ItemClass.IrritianUnzipper))
yellow_shop.append(item(ItemClass.Aglu)) 
yellow_shop.append(item(ItemClass.Repair))
yellow_shop.append(item(ItemClass.MetaController))
yellow_shop.append(item(ItemClass.IrritianEngine)) 
yellow_shop.append(item(ItemClass.IrritianEngine2))
yellow_shop.append(item(ItemClass.IrritianMiner))
yellow_shop.append(item(ItemClass.IrritianInfantry))
yellow_shop.append(item(ItemClass.IrritianArmored))
yellow_shop.append(item(ItemClass.ITrash))
