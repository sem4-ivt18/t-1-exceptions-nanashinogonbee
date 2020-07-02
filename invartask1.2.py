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


if __name__ == '__main__':
    assert list(
        read_json('example.json')
        ) == ['glossary'], 'Level 1 nesting error'
    assert list(
        read_json('example.json')['glossary']
        ) == ['title', 'GlossDiv'], 'Level 2 nesting error'
    assert read_json(
        'example.json'
        )['glossary']['title'] == 'example glossary', 'Level 3 nesting error'

result = read_json('example.json')
print(result)
