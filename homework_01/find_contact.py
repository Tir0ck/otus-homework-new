import json
from homework_01.common import PATH


def find_one_contact():
    search_parameter = ''
    confirmation = ''
    search_result = []

    while not search_parameter:
        search_parameter = input(
            '\nВыберите параметр для поиска (1, 2, 3):\n'
            '1. Имя\n'
            '2. Номер телефона\n'
            '3. Комментарий\n'
            '0. Выход\n'
        )

        if search_parameter in ('1', '2', '3'):
            continue
        elif search_parameter == '0':
            return
        else:
            search_parameter = ''
            print('Вы ввели некорректное значение!')

    condition = 'name'

    if search_parameter == '2':
        condition = 'phone'
    elif search_parameter == '3':
        condition = 'comment'

    search_query = input('\nВведите поисковый запрос:\n').lower()

    with open(PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for contact in data['contacts']:
        match = False
        for key, value in contact.items():
            if key == condition and search_query in value.lower():
                match = True
        if match:
            search_result.append(contact)

    print('Результат поиска:\n')
    print(json.dumps(search_result, indent=4, ensure_ascii=False))

    while not confirmation:
        confirmation = input('Хотите продолжить поиск? (да\\нет)\n').lower()
        if confirmation == 'да':
            find_one_contact()
        elif confirmation == 'нет':
            print('\nВы завершили поиск\n')
        else:
            confirmation = ''
            print('Вы ввели некорректное значение!\n')


# find_one_contact()
