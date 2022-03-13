


class EntitySetter:
    def set_space_object(self, SpaceObject):
        SpaceObject.set_entity(self)

    def remove_space_object(self):
        self.SpaceObject.remove_entity(self)

    def entry_entity(self):
        self.SpaceObject.entry_entity(self)

    def exit_entity(self):
        self.SpaceObject.exit_entity(self)
