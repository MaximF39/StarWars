
class Clan:

    def __init__(self, Game, dict_):
        self.name = dict_['name']
        self.Game = Game
        self.lider = getattr(self.Game, f'Player_{dict_["lider_id"]}')



    def accept_new_player(self):
        pass

    def appoint_player(self):
        pass

    def rename_clan(self):
        pass

    def rename_description(self):
        pass
