from python.Game.Game.SpaceObjects import item


class AdminPanel:

    def __init__(self, Game):
        self.Game = Game

    def process(self):
        text = input('Command:')
        text = text.split()
        match text[0]:
            case "1":
                self.to_send_player_2_item(text[1], text[2], text[3])

    def to_send_player_2_item(self, player_id, items_cn, wear):
        # player_id = kwargs['player_id']
        # items_cn = kwargs['item_cn']
        # wear = kwargs['wear']


        if hasattr(self.Game, f"Player_{player_id}"):
            Player = getattr(self.Game, f"Player_{player_id}")
            Item_ = item(class_number=items_cn, wear=wear, Game=self.Game, OwnerClass=Player)
            Player.add_item(Item_)


