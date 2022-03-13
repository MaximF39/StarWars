from python.Game import Mob_SpaceObjectSetter
from python.Game import Player_SpaceObjectSetter


class I_SpaceObjectSetter(Mob_SpaceObjectSetter, Player_SpaceObjectSetter):
    
    def __init__(self):
        super().__init__()
    
    def _set_entity(self, Entity):
        name_entity = Entity.__class__.__name__
        match name_entity:
            case "B_Player":
                super()._set_player(Entity)
            case "Mob":
                super()._set_mob(Entity)

    def _entry_entity(self, Entity):
        name_entity = Entity.__class__.__name__
        match name_entity:
            case "B_Player":
                super()._entry_player(Entity)
            case "Mob":
                super()._entry_mob(Entity)
            
    def _remove_entity(self, Entity):
        name_entity = Entity.__class__.__name__
        match name_entity:
            case "B_Player":
                super()._remove_player(Entity)
            case "Mob":
                super()._remove_mob(Entity)
            
    def _exit_entity(self, Entity):
        name_entity = Entity.__class__.__name__
        match name_entity:
            case "B_Player":
                super()._exit_player(Entity)
            case "Mob":
                super()._exit_mob(Entity)