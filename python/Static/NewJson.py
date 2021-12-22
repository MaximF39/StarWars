import json
import pathlib

# from python.MyUtils.DotMap import DotMap

bs = pathlib.Path(__file__).parent.joinpath('Json')
id_parse = ['Clans', "GalaxyMap"]
guid_parse = ['AmmoParameters', "DeviceParameters", "DroidParameters",
              "EngineParameters", "ShipParameters", "WeaponParameters", "ResourseParameters"]


def _get_path_json(text: str) -> pathlib.Path:
    if text.split('.')[-1] == 'json':
        return bs.joinpath(text)
    else:
        return bs.joinpath(text + '.json')


def new(file_name):
    id_ = 0
    with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
        res = json.loads(f.read())
        for i in res:
            if len(i["SpaceObjects"]["data"]):
                for space_object in i["SpaceObjects"]["data"]:
                    id_ += 1
                    space_object['id'] = id_

    with open(_get_path_json(file_name), 'w', encoding='utf-8-sig') as f:
        json.dump(res, f)


print(new("GalaxyMap"))
