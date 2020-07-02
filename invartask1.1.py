import json

def read_json(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print('A bruh moment occurred while reading the JSON file')

    try:
        return json.load(f)
    except json.decoder.JSONDecodeError:
        print('A bruh moment occurred while parsing the JSON file')


print(read_json('example.json'))
