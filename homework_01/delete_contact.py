import json
from pprint import pprint
from homework_01.common import PATH
from homework_01.common import check_contact_id


def remove_contact():
    contact_id = ''
    confirmation = ''

    while not contact_id:
        with open(PATH, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        pprint(data['contacts'], compact=False, indent=4, width=200, sort_dicts=False)

        contact_id = input('\nВведите номер ИД для удаления контакта:\n')

        contact_id = check_contact_id(data, contact_id)

    temp_contact = [contact for contact in data['contacts'] if contact['id'] == contact_id]

    while not confirmation:
        confirmation = input(f'\nВы точно хотите удалить контакт(да\\нет): \n{temp_contact}\n')

        if confirmation == 'нет':
            return
        elif confirmation == 'да':
            continue
        else:
            confirmation = ''
            print('Вы ввели некорректное значение!')

    data['contacts'] = [contact for contact in data['contacts'] if contact['id'] != contact_id]

    with open(PATH, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print('Вы успешно удалили контакт!\n')

    pprint(data['contacts'], sort_dicts=False, width=200)


# remove_contact()
