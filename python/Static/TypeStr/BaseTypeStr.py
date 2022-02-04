class BaseTypeStr:
    def get_str(self, int_):
        for i in self.data:
            if int_ == i[1]:
                return i[0]