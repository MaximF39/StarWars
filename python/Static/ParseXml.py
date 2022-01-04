import json
import pathlib

from python.Utils.DotMap import DotMap

bs = pathlib.Path(__file__).parent.joinpath('Json')
__id_parse = ['Clan', "GalaxyMap"]
__guid_parse = ['AmmoParameters', "DeviceParameters", "DroidParameters",
              "EngineParameters", "ShipParameters", "WeaponParameters", "ResourseParameters"]

def _get_path_json(text: str) -> pathlib.Path:
    if text.split('.')[-1] == 'json':
        return bs.joinpath(text)
    else:
        return bs.joinpath(text + '.json')

def parse_xml(file_name) -> list:
    with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
        res = json.loads(f.read())
        return res

def item_id(id_):
    for file_name in __guid_parse:
        with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for item in res:
                if item['classNumber'] == id_:
                    return item