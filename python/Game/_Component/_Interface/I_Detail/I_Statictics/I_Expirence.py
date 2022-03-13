from python.Game._Component.Body.B_Entity.B_Statistics.B_Experience import B_Experience
from python.Game._Component.Event.E_Entity.E_Statistics.E_Experience import E_Experience


class I_Experience(B_Experience, E_Experience):

    def __init__(self, experience):
        super().__init__(experience)

