from python.Config.CFG_Player.Statistics.cfg_rating import get_rating_for_kill


class Rating:
    rating: int

    def sub_rating(self, rating):
        self.__get_rating(-rating)

    def get_rating(self, rating):
        self.__get_rating(rating)

    def get_rating_for_kill(self, Whom, coef):
        if hasattr(Whom, "rating"):
            rating = get_rating_for_kill(Whom, coef)
            self.get_rating(rating)

    def __get_rating(self, rating):
        self.rating += rating
