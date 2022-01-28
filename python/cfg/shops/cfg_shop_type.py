from python.Static.Type.ShopType import ShopType
from python.cfg.shops.ships import *

default_shop = [*weak_system, *medium_system, *strong_system] # system

default_type = [ShopType.InventoryShop, ShopType.ShipFactory]

repository = [ShopType.Repository, ShopType.Angar, ShopType.ClanRepository]

update_resources_shop = [17]
update_resources_type = [8]

