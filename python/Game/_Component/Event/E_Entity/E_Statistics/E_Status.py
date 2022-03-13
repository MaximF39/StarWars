class E_Status:
    """
    police = 1
    pirate = -1
    """
    __status: int
    level:int

    def __add__(self, other):
        if isinstance(other, int):
            self.__change_status(other)

    def __sub__(self, other):
        if isinstance(other, int):
            self.__change_status(-other)

    def __change_status(self, status):
        self.__status -= status