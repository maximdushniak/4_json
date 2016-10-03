import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        print('Файл не найден')
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    if data is not None:
        try:
            print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))
        except ValueError:
            print(data)


if __name__ == '__main__':
    filepath = input(u'Имя файла [data.json]: ')
    if not filepath:
        filepath = 'data.json'
    data = load_data(filepath)
    pretty_print_json(data)