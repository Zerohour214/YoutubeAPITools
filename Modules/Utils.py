import json


def import_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            json.dump([], file, indent=4)
        return []


def export_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
