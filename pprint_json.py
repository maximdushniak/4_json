import json


def load_data(filepath):
    data = []
    with open(filepath, encoding='utf-8') as datafile:
        data = json.load(datafile)
    return data


def pretty_print_json(data):
    # json.dumps(data, sort_keys=True, indent=4)
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    filepath = input(u'Имя файла [data.json]: ')
    if not filepath:
        filepath = 'data.json'
    data = load_data(filepath)
    pretty_print_json(data)