if False:
    from python.Player.Player import Player

class SetPlayer:
    players:list["Player"] = []

    def set_player(self, Player):
        self.players.append(Player)
        Player.set_space_object(self)

    def remove_player(self, Player):
        if Player in self.players:
            self.players.remove(Player)