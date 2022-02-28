class Drop:
    __REQ = ["x", "y", "wear", "classNumber"]

    def __init__(self, data):
        self.__check_data(data)
        self.__dict__.update(data)

    def get_drop(self):
        return self.__dict__

    def __check_data(self, data):
        for param in self.__REQ:
            if not param in data:
                raise NotImplementedError(f"Not found {param}")
