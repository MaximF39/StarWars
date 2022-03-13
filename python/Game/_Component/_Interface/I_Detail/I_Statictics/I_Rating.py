from python.Game._Component.Body.B_Entity.B_Statistics import B_Rating
from python.Game._Component.Event.E_Entity.E_Statistics.E_Rating import E_Rating


class I_Rating(B_Rating, E_Rating):

    def __init__(self, rating):
        super().__init__(rating)