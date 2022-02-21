if False:
    from python.Player.Player import Player

class SetPlayer:

    def __init__(self):
        self.players:list["DB_Player"] = []

    def set_player(self, Player):
        self.players.append(Player)
        Player.set_space_object(self)

    def remove_player(self, Player):
        if Player in self.players:
            Player.not_target()
            self.players.remove(Player)