import json
from pprint import pprint
from homework_01.common import PATH


def create_id(data):
    if len(data['contacts']) == 0:
        return '1'
    if len(data['contacts']) < int(data['contacts'][-1]['id']):
        return str(int(data['contacts'][-1]['id']) + 1)
    else:
        return str(len(data['contacts']) + 1)


def create_contact():
    temp_contact = {}
    confirmation = ''

    while not temp_contact:

        name = input('Введите имя:\n')
        phone = input('Введите телефон:\n')
        comment = input('Введите комментарий:\n')

        temp_contact = {
            'name': name,
            'phone': phone,
            'comment': comment,
        }

        while not confirmation:
            confirmation = input(
                f'\nВы хотите добавить контакт? (да\\нет) \n'
                f'{json.dumps(temp_contact, ensure_ascii=False, indent=4)}\n'
            )

            if confirmation == 'да':
                continue
            elif confirmation == 'нет':
                return
            else:
                confirmation = ''
                print('Вы ввели некорректное значение!')

    with open(PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    data['contacts'].append(
        {
            'id': create_id(data),
            'name': temp_contact['name'],
            'phone': temp_contact['phone'],
            'comment': temp_contact['comment'],
        }
    )

    with open(PATH, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print('\nКонтакт успешно добавлен\n')
    pprint(data['contacts'], indent=4, width=300, sort_dicts=False)


# create_contact()
