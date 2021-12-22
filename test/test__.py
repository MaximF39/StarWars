
import json

data = {'ss': 22, 'ee':33}
with open('ttttt.json', 'a', encoding='utf-8-sig') as f:
    json.dump(data, f)