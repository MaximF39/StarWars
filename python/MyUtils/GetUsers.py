import redis
import json


def json_all_users_update_log_passwd():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    jsn = {}
    for i in r.keys():
        name = i.decode()
        jsn[name] = r.get(name).decode()
    print(jsn)
    with open("users_log_passwd.json", 'w') as f:
        json.dump(jsn, f)


if __name__ == '__main__':
    json_all_users_update_log_passwd()
