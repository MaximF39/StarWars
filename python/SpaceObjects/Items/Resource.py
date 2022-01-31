from python.BaseClass.BaseItem.Quantitative import Quantitative
from python.Packages.PackagesManager import PackagesManager


class Resource(Quantitative):

    def __init__(self, Game, classNumber, OwnerClass, count):
        super().__init__(Game, classNumber, OwnerClass, count)