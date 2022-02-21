
class Rating:
    rating: int

    def sub_rating(self, rating):
        self.__get_rating(-rating)

    def get_rating(self, rating):
        self.__get_rating(rating)

    def __get_rating(self, rating):
        self.rating += rating
