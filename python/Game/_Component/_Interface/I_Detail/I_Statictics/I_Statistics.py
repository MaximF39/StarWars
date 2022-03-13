from python.Game._Component._Interface.I_Detail.I_Statictics.I_Expirence import I_Experience
from python.Game._Component._Interface.I_Detail.I_Statictics.I_Rating import I_Rating
from python.Game._Component._Interface.I_Detail.I_Statictics.I_Status import I_Status


class I_Statistics(I_Experience, I_Status, I_Rating):

    def __init__(self, experience, status, rating):
        I_Experience.__init__(self, experience)
        I_Status.__init__(self, status)
        I_Rating.__init__(self, rating)
