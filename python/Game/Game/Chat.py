from python.Static.Type.Keys import Keys
from python.Static.Type.T_Message import T_Message

if False:
    from python.Server import Server


class Chat: # Наследуется от StarWars
    players: list["CFG_Player"]
    Server: "Server"

    def __init__(self, Server: "Server"):
        self.Server = Server

    def init_game(self, Game):
        self.Game: "StarWars" = Game

    def get_players(self, chat_type, id_):
        match chat_type:
            case T_Message.GLOBAL:
                return self.Server.players
            case T_Message.LOCAL:
                return getattr(self.Game, f"Player_{id_}").Location.players
            case T_Message.CLAN:
                if hasattr(getattr(self.Game, f"Player_{id_}"), 'Clan'):
                    return getattr(self.Game, f"Player_{id_}").Clan.players_online
            case T_Message.CLIENTCHAT:
                pass
            case T_Message.TRADE:
                pass

    def send_message(self, Player:"PlayerItems", data):
        players = self.get_players(data[Keys.TYPE_CHAT], Player.id)
        for Player in players:
            Player.message(Player, data)
