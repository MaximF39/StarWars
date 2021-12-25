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
                    space_object['shop'] = []
                    id_ += 1
                    space_object['id'] = id_
                    if space_object['type'] == 2:
                        space_object['shop'] = [{'id': 10004, 'type': 4}, {'id': 10005, 'type': 5}, {'id': 10009, 'type': 9}]
            if i['Planets']['data']:
                for dict_planet in i['Planets']['data']:
                    dict_planet['shop'] = []
                    if dict_planet['race']:
                        dict_planet['shop'] = [{'id': dict_planet['id'], 'type':1}]
                        if dict_planet['id'] < 50:
                            dict_planet['shop'].append({'id': dict_planet['race'], 'type': 2})
                        if dict_planet['id'] == 118:
                            dict_planet['shop'].append({'id': 10008, 'type': 8})



    with open(_get_path_json(file_name), 'w', encoding='utf-8-sig') as f:
        json.dump(res, f)


print(new("GalaxyMap"))
