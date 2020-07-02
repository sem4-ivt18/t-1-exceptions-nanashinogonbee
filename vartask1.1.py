import json

schema = {
    'name': '',
    'fav_anime': '',
    'roma_vlogs': False,
    'comment': '',
    }

schema['name'] = input('Введи имя: ') or schema['name']
schema['fav_anime'] = input('Введи любимый тайтл: ') or schema['fav_anime']
schema['roma_vlogs'] = bool(
    input('Напиши сюда что-нибудь, если смотрел влоги Ромы: ')
    )
schema['comment'] = input(
    'Сюда можно просто что-нибудь написать: '
    ) or schema['comment']

try:
    with open('result.json', 'r') as json_file:
        try:
            decoded = json.load(json_file)
        except json.decoder.JSONDecodeError:
            decoded = []
except FileNotFoundError:
    decoded = []

decoded.append(schema)

with open('result.json', 'w') as json_file:
    json.dump(decoded, json_file)

