import json
import pathlib
from Type.ItemClass import ItemClass as Items

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


def new_galaxy(file_name):
    with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
        res = json.loads(f.read())
        for i in res:
            if len(i["SpaceObjects"]["data"]):
                for space_object in i["SpaceObjects"]["data"]:
                    space_object['shops'] = []
                    space_object['id'] = -1 * space_object['type']
                    match space_object['type']:
                        case 2:
                            space_object['shops'] = [{'id': -4, 'type': 4}, {'id': -5, 'type': 5}, {'id': -9, 'type': 9}]

            if i['Planets']['data']:
                for dict_planet in i['Planets']['data']:
                    dict_planet['shops'] = []
                    dict_planet['ships'] = []
                    dict_planet['inventory'] = [{'classNumber': 2}, {'classNumber': 12},]
                    if dict_planet['race']:
                        match dict_planet['race']:
                            case 4:
                                dict_planet['inventory'] = [
                                    {'classNumber':Items.LaserGun}, {'classNumber':Items.Battery},  {'classNumber':Items.MedramillUnzipper},
                                    {'classNumber':Items.Shield}, {'classNumber':Items.Energon}, {'classNumber':Items.MAntiFazer},
                                    {'classNumber':Items.RepairDroid}, {'classNumber':Items.MRepair2}, {'classNumber':Items.MedramillEngine},
                                    {'classNumber':Items.MedramillEngine2}, {'classNumber':Items.MedramilMiner},
                                    {'classNumber':Items.MedramillInfantry}, {'classNumber':Items.MedramillArmored}, {'classNumber':Items.MTrash}]
                            case 3:
                                dict_planet['inventory'] = [{'classNumber':Items.AnidRezak}, {'classNumber':Items.AnidUnzipper}, {'classNumber':Items.Turbo}, {'classNumber':Items.Processor}, {'classNumber':Items.Nitrinium},
                                                                                                     {'classNumber':Items.AnidEngine}, {'classNumber':Items.AnidEngine2}, {'classNumber':Items.AnidMiner}, {'classNumber':Items.AnidInfantry},
                                                                                                                                                               {'classNumber':Items.AnidArmored}, {'classNumber':Items.ATrash}]
                            case 1:
                                dict_planet['inventory'] = [{'classNumber':Items.OmolenianRezak}, {'classNumber':Items.OmolenianUnzipper}, {'classNumber':Items.Generator}, {'classNumber':Items.Damage},
                                                                                                {'classNumber':Items.Armor}, {'classNumber':Items.Phaser}, {'classNumber':Items.OmolenianEngine}, {'classNumber':Items.OmolenianEngine2},
                                                                                                                                                      {'classNumber':Items.OmolenianEngine3}, {'classNumber':Items.OmolenianMiner}, {'classNumber':Items.OmolenianInfantry},
                                                                                                                                                                                                       {'classNumber':Items.OmolenianArmored}, {'classNumber':Items.OTrash}]
                            case 2:
                                dict_planet['inventory'] =  [{'classNumber':Items.Jalo}, {'classNumber':Items.IrritianUnzipper}, {'classNumber':Items.Aglu}, {'classNumber':Items.Repair}, {'classNumber':Items.MetaController},
                                                                                                {'classNumber':Items.IrritianEngine}, {'classNumber':Items.IrritianEngine2}, {'classNumber':Items.IrritianMiner},
                                                                                                                                                {'classNumber':Items.IrritianInfantry}, {'classNumber':Items.IrritianArmored}, {'classNumber':Items.ITrash}]

                        dict_planet['shops'] = [{'id': dict_planet['id'], 'type':1}]
                        if dict_planet['id'] < 50:
                            dict_planet['ships'] = [{'ship_class':10}, {'ship_class': 4}]
                            dict_planet['shops'].append({'id': -2, 'type': 2})
                        if dict_planet['id'] == 118:
                            dict_planet['shops'].append({'id': -8, 'type': 8})



    with open(_get_path_json(file_name), 'w', encoding='utf-8-sig') as f:
        json.dump(res, f)

print(new_galaxy("GalaxyMap"))
