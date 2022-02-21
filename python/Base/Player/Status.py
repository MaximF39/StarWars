

import numpy
class Status:
    """
    police = 1
    pirate = -1
    """
    status: int
    points:int

    def __init__(self):
        self.__update_status()

    def __update_status(self):
        self.pirateStatus = 0 if self.status > 0 else self.status
        self.policeStatus = 0 if 0 > self.status else self.status

    def get_status(self, count):
        self.__get_status(count)

    def __get_status(self, status):
        self.status += status
        self.__update_status()
        self.__check_level()

    def __check_level(self):
        pass

    def __change_status_lvl(self, count):
        self.status += count