from python.SpaceObjects.Item import item
from python.Static.Type.ItemClass import ItemClass
from python.Static.Type.Race import Race


def get_default_items(race, OwnerClass, Game):
    return (item(classNumber=item_classNumber, Game=Game, count=count, OwnerClass=OwnerClass) for item_classNumber in get_shop_by_race[race])

count = 1000

green_shop_items = (
        ItemClass.AnidRezak,
        ItemClass.AnidUnzipper,
        ItemClass.Turbo,
        ItemClass.Processor,
        ItemClass.Nitrinium,
        ItemClass.AnidEngine,
        ItemClass.AnidEngine2,
        ItemClass.AnidMiner,
        ItemClass.AnidInfantry,
        ItemClass.AnidArmored,
        ItemClass.ATrash,
    )
blue_shop_items = (
        ItemClass.LaserGun,
        ItemClass.Battery,
        ItemClass.MedramillUnzipper,
        ItemClass.Shield,
        ItemClass.Energon,
        ItemClass.MAntiFazer,
        ItemClass.RepairDroid,
        ItemClass.MRepair2,
        ItemClass.MedramillEngine,
        ItemClass.MedramillEngine2,
        ItemClass.MedramilMiner,
        ItemClass.MedramillInfantry,
        ItemClass.MedramillArmored,
        ItemClass.MTrash,
    )
red_shop_items = (
        ItemClass.OmolenianRezak,
        ItemClass.OmolenianUnzipper,
        ItemClass.Generator,
        ItemClass.Damage,
        ItemClass.Armor,
        ItemClass.Phaser,
        ItemClass.OmolenianEngine,
        ItemClass.OmolenianEngine2,
        ItemClass.OmolenianEngine3,
        ItemClass.OmolenianMiner,
        ItemClass.OmolenianInfantry,
        ItemClass.OmolenianArmored,
        ItemClass.OTrash,
    )
yellow_shop_items = (
        ItemClass.Jalo,
        ItemClass.IrritianUnzipper,
        ItemClass.Aglu,
        ItemClass.Repair,
        ItemClass.MetaController,
        ItemClass.IrritianEngine,
        ItemClass.IrritianEngine2,
        ItemClass.IrritianMiner,
        ItemClass.IrritianInfantry,
        ItemClass.IrritianArmored,
        ItemClass.ITrash,
)

get_shop_by_race = {
Race.OMOLENIAN_ID: red_shop_items, #OMOLENIAN_ID
Race.IRRIITIAN_ID: yellow_shop_items, #IRRIITIAN_ID
Race.ANID_ID: green_shop_items, #ANID_ID
Race.MEDRAMIL_ID: blue_shop_items, #MEDRAMIL_ID
}

