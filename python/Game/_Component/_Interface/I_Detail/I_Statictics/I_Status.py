from python.Game._Component.Body.B_Entity.B_Statistics.B_Status import B_Status
from python.Game._Component.Event.E_Entity.E_Statistics.E_Status import E_Status


class I_Status(B_Status, E_Status):

    def __init__(self, status):
        super().__init__(status)