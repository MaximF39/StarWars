from . import SpaceObject


class Item(SpaceObject):
    guid: bytes
    price: int
    inUsing: bool
    class_number: int

    def __init__(self, data):
        super().__init__(data)
        self.guid = self.__create_guid()

    def __create_guid(self):
        import uuid
        return uuid.uuid4().bytes
