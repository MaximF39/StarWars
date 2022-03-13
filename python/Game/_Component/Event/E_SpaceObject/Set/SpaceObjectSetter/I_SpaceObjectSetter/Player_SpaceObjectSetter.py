from python.Game import B_SpaceObjectSetter


class Player_SpaceObjectSetter(B_SpaceObjectSetter):

    def __init__(self):
        super().__init__()
        self.players = []

    def _set_player(self, Player):
        super()._set_entity(Player)
        self.players.append(Player)

    def _entry_player(self, Player):
        super()._entry_entity(Player)
        self.players.append(Player)

    def _remove_player(self, Player):
        super()._remove_entity(Player)
        self.players.remove(Player)

    def _exit_player(self, Player):
        super()._remove_entity(Player)
        self.players.remove(Player)


    def _send_package_players(self, *PackageNumber):
        for Player in self.players:
            Player.SendPacMan(*PackageNumber)
