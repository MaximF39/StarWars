from python.Packages.Packages.BP_Reader.B_PackagesEventOrganizer import B_PackagesEventOrganizer


class PackagesReader(B_PackagesEventOrganizer):
    def __init__(self, Game, Player, command_type, data):
        B_PackagesEventOrganizer.__init__(self, Game, Player, command_type, data)
