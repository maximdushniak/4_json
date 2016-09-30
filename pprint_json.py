import json


def load_data(filepath):
    data = []
    with open(filepath) as datafile:
        data = json.loads(datafile.read())
    return data


def pretty_print_json(data):
    pass


if __name__ == '__main__':
    filepath = input(u'Имя файла [data.json]: ')
    if not filepath:
        filepath = 'data.json'
    data = load_data(filepath)
    pretty_print_json(data)