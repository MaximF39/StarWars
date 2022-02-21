from python.Static.Type.Message import Message

if False:
    from python.Vacuum_Server import Server
    from python.StarWars import StarWars
    from python.Player.Player import Player


class Chat: # Наследуется от Game
    players: list["DB_Player"]
    Server: "Server"

    def __init__(self, Server: "Server"):
        self.Server = Server

    def init_game(self, Game):
        self.Game:"StarWars" = Game

    def get_players(self, chat_type, id_):
        match chat_type:
            case Message.GLOBAL:
                return self.Server.players
            case Message.LOCAL:
                return getattr(self.Game, f"Player_{id_}").Location.players
            case Message.CLAN:
                if hasattr(getattr(self.Game, f"Player_{id_}"), 'DB_Clan'):
                    return getattr(getattr(self.Game, f"Player_{id_}"), 'DB_Clan').players_online
            case Message.CLIENTCHAT:
                pass
            case Message.TRADE:
                pass

    def send_message(self, Player:"PlayerItems", data):
        players = self.get_players(data['type_chat'], Player.id)
        for Player in players:
            Player.PacMan.message(Player, data)
