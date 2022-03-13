class E_Rating:
    rating:int

    def __add__(self, other):
        if isinstance(other, int):
            self.__change_rating(other)

    def __sub__(self, other):
        if isinstance(other, int):
            self.__change_rating(-other)

    def __change_rating(self, rating):
        self.rating += rating