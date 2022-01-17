import json
import pathlib
from Type.ItemClass import ItemClass as Items

# from python.Utils.DotMap import DotMap

bs = pathlib.Path(__file__).parent.joinpath('Json')
id_parse = ['Clan', "GalaxyMap"]
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

new_items()

# print(new_galaxy("GalaxyMap"))
