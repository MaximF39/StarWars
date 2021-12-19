import json
import pathlib

from python.MyUtils.DotMap import DotMap

bs = pathlib.Path(__file__).parent.joinpath('Xml')
id_parse = ['Clans', "GalaxyMap"]
guid_parse = ['AmmoParameters', "DeviceParameters", "DroidParameters",
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