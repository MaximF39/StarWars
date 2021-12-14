from . import Location, parse_location


class Sector:
    id: int
    name: str

    def __init__(self, id_):
        self.id = id_
        self.create_locations()

    def create_locations(self):
        data_all_location = parse_location()
        for data_loc in data_all_location:
            if data_loc['Sector'] == self.id:
                id_ = data_loc['id']
                setattr(self, f'location_{id_}', Location(data_loc))

