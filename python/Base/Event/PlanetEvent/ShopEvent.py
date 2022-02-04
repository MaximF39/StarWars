
class ShopEvent:

    def open_shop(self, data):
        match data['type']:
            case 1:
                self.SpaceObject.inventory_shop(self)
            case 2:
                self.SpaceObject.ship_factory(self)
            case 3:
                self.SpaceObject.ginetic_lab(self)
            case 4:
                self.SpaceObject.repository(self)
            case 5:
                self.SpaceObject.angar(self)
            case 6:
                self.SpaceObject.update_ships(self)
            case 8:
                self.SpaceObject.update_resources(self)
            case 9:
                self.SpaceObject.clan_repository(self)
