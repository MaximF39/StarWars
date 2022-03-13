class B_Status:
    """
    police = 1
    pirate = -1
    """

    def __init__(self, status):
        self.__status = status
        self.__level = self.__get_level()
        self.pirate_status = self.__get_pirate_status()
        self.police_status = self.__get_police_status()

    @property
    def status(self):
        return self.__status

    @property
    def level(self):
        return self.__level

    def __get_level(self):
        return 1

    def __get_pirate_status(self):
        return 0 if self.status > 0 else self.status

    def __get_police_status(self):
        return 0 if 0 > self.status else self.status