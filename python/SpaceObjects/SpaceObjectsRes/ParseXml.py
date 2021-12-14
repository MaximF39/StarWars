import json
import pathlib



bs = pathlib.Path(__file__).parent.joinpath('Xml')
id_parse = ['Clans', "GalaxyMap"]
guid_parse = ['AmmoParameters', "DeviceParameters", "DroidParameters",
              "EngineParameters", "ShipParameters", "WeaponParameters", "ResourseParameters"]

def _get_path_json(text: str) -> pathlib.Path:
    return bs.joinpath(text + '.json')

def parse_location() -> list:
    with open(_get_path_json("GalaxyMap"), 'r', encoding='utf-8-sig') as f:
        res = json.loads(f.read())
        return res