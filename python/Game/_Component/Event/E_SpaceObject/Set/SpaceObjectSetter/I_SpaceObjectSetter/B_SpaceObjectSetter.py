

class B_SpaceObjectSetter:

    def __init__(self):
        self.entities = []

    def _set_entity(self, Entity):
        self.entities.append(Entity)
        Entity.SpaceObject = self

    def _remove_entity(self, Entity):
        self.entities.remove(Entity)
        Entity.SpaceObject = None

    def _entry_entity(self, Entity):
        self.entities.append(Entity)

    def _exit_entity(self, Entity):
        self.entities.remove(Entity)