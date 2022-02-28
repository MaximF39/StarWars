if False:
    pass


class SetPlayer:
    def __init__(self):
        self.players: list["CFG_Player"] = []

    def _set_player(self, Player):
        self.players.append(Player)
        Player.set_space_object(self)

    def _remove_player(self, Player):
        if Player in self.players:
            Player.not_target()
            self.players.remove(Player)

    def send_all_player_packages(self, *PackagesNumber):
        for Player in self.players:
            for PackageNumber in PackagesNumber:
                Player.Packages.SendPacMan(PackageNumber)