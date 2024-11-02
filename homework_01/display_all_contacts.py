import json
from pprint import pprint
from homework_01.common import PATH


def display_all():
    with open(PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    pprint(data['contacts'], indent=4, width=300, sort_dicts=False)
