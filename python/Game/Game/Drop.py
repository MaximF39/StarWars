from python.Static.Type.Keys import Keys

class Drop:
    # __REQ = [Keys.X, Keys.Y, Keys.class_number]

    def __init__(self, data):
        self.__check_data(data)
        self.__dict__.update(data)

    def get_drop(self):
        return self.__dict__

    def __check_data(self, data):
        return
        for param in self.__REQ:
            if not param in data:
                raise NotImplementedError(f"Not found {param}")
