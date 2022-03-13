from python.Game._Component.Body.B_Item.B_BaseItem.B_BaseItem import B_BaseItem


class Quantitative(B_BaseItem):
    count: int
    mod = 'q'
    drop = True

    def __init__(self, Game, data, Owner):
        B_BaseItem.__init__(self, Game, data, Owner)
        self.count = self.wear

    def drop(self, count):
        Player = self.Owner
        B_BaseItem.set_x_y_owner(self)
        if self.count == count:
            self.transfer(self.Owner.Location)
        elif self.count > count:
            new_item = self - count
            self.Owner.Location.add_item(new_item)
        Player.SendPacMan.items()

    def buy(self, Player, count):
        if B_BaseItem.check_default_shop(self):
            class_ = self.copy_class()
            class_.separation(Player, count)
        else:
            self.separation(Player, count)
        B_BaseItem.good_trade(self, Player)

    def sell(self, Planet, count):
        Player = self.Owner
        self.separation(Planet, count)
        B_BaseItem.good_trade(self, Player)

    def separation(self, Whom, /, count=None, all_=None):
        if count is None and all_ is None:
            raise NotImplementedError('Забыл указать элемент?')
        if all_ or self.count == count:
            self.transfer(Whom)
        elif self.count > count:
            new_item = self - count
            Whom.add_item(new_item)

    def __add__(self, other):
        self._here_type(other, self)
        self.count += other.count
        return self

    def __sub__(self, other):
        if self.count - other >= 0:
            self._here_type(other, int())
            self.count -= other
            class_ = self.copy_class()
            class_.count = other
            if self.count == 0:
                self.Owner.remove_item(self)
            else:
                self.Owner.change_hold(class_.get_size)
            return class_
        else:
            raise NotImplementedError('Почему число отрицательное шмоток?')
