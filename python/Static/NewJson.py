import json
import pathlib

# from python.Utils.DotMap import DotMap

bs = pathlib.Path(__file__).parent.joinpath('Json')
id_parse = ['DB_Clan', "GalaxyMap"]
guid_parse = ['AmmoParameters', "DeviceParameters", "DroidParameters",
              "EngineParameters", "ShipParameters", "WeaponParameters", "ResourseParameters"]


def _get_path_json(text: str) -> pathlib.Path:
    if text.split('.')[-1] == 'json':
        return bs.joinpath(text)
    else:
        return bs.joinpath(text + '.json')


def new_items():
    guid_parse2 = {'AmmoParameters':2, "DeviceParameters":5, "DroidParameters": 6,
              "EngineParameters":3, "ShipParameters":7, "WeaponParameters":4, "ResourseParameters":1}
    for key, value in guid_parse2.items():
        with open(_get_path_json(key), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for i in res:
                i['Types'] = value
                i['wear'] = 1
                i['level'] = 0

        with open(_get_path_json(key), 'w', encoding='utf-8-sig') as f:
            json.dump(res, f)

# new_items()
def X_sector():
    file_name  = "ShipParameters"
    with open(_get_path_json(file_name), "r", encoding='utf-8-sig') as f:
        res = json.load(f)
    # dont_location_id = [68, 69, 70, 71, 92, 60, 64, 54, 95, 52]
    dont_location_id = [75, 74, 23, 26, 21, 20, 14, 72, 73]
    for element in res:
        element['maxDroids'] = 2
        # element['effects'] = element['effects']['data']
        # element['restrictions'] = element['restrictions']['data']
        # element['features'] = element['features']['data']
        # element['CN_ammo'] = element['ammoClass']
        # del element['ammoClass']
        # del element['maxWear']
        # del element['wear']
        # del element['Types']
        # del element['guid']
        # del element['level']
        # del element['inUsing']
        # del element['satisfying']
    #     location['map_x'] = location['x']
    #     location['map_y'] = location['y']
    #     del location['x'], location['y']
        # del location['Types']
        # location['Planets'] = location['Planets']['data']
        # location['SpaceObjects'] = location['SpaceObjects']['data']
        # if location["id"] in dont_location_id:
        #     for planet in location['Planets']['data']:
        #         if planet['classNumber'] < 6:
        #             continue
        #         planet["aliance"] = 4
        #         planet["race"] = 6
    with open(_get_path_json(file_name), "w", encoding='utf-8-sig') as f:
        json.dump(res, f, ensure_ascii=False)

# X_sector()


