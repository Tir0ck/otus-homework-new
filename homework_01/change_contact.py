import json
from pprint import pprint
from homework_01.common import PATH
from homework_01.common import check_contact_id


def update_contact():
    contact_id = ''
    confirmation = ''
    parameter = ''
    temp_contact = {
        'index_in_list': None,
        'contact': {},
    }

    while not contact_id:
        with open(PATH, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        pprint(data['contacts'], compact=False, indent=4, width=200, sort_dicts=False)

        contact_id = input('\nВведите номер ИД для изменения контакта:\n')

        contact_id = check_contact_id(data, contact_id)

    for index, contact in enumerate(data['contacts']):
        if contact['id'] == contact_id:
            temp_contact['index_in_list'] = index
            temp_contact['contact'] = contact

    while not confirmation:
        confirmation = input(f'\nВы точно хотите изменить контакт(да\\нет): \n{temp_contact['contact']}\n')

        if confirmation == 'нет':
            return
        elif confirmation == 'да':
            continue
        else:
            confirmation = ''
            print('Вы ввели некорректный ответ!\n')

    while not parameter:
        parameter = input(
            'Выберите параметр для изменения(1, 2, 3):\n'
            '1. Имя\n'
            '2. Номер телефона\n'
            '3. Комментарий\n'
            '0. Выход\n'
        )

        if parameter in ('1', '2', '3', '0'):
            continue
        else:
            parameter = ''
            print('Вы ввели некорректное значение!!!\n')

    if parameter == '1':
        temp_contact['contact']['name'] = input('\nВведите новое имя:\n')
    elif parameter == '2':
        temp_contact['contact']['phone'] = input('\nВведите новый номер телефона:\n')
    elif parameter == '3':
        temp_contact['contact']['comment'] = input('\nВведите новый комментарий:\n')
    elif parameter == '0':
        return

    data['contacts'].pop(temp_contact['index_in_list'])
    data['contacts'].insert(temp_contact['index_in_list'], temp_contact['contact'])

    with open(PATH, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(
        '\nКонтакт успешно изменен!\n'
        f'{temp_contact['contact']}\n'
    )


# update_contact()
