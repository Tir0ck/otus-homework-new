from homework_01.change_contact import update_contact
from homework_01.delete_contact import remove_contact
from homework_01.display_all_contacts import display_all
from homework_01.create_new_contact import create_contact
from homework_01.find_contact import find_one_contact


def menu():
    in_menu = True

    while in_menu:
        menu_points = (
            '\nМеню справочника:\n'
            'Введите цифру для выбора действия\n'
            '\n'
            '1. Показать все контакты\n'
            '2. Создать контакт\n'
            '3. Найти контакт\n'
            '4. Изменить контакт\n'
            '5. Удалить контакт\n'
            '0. Выход\n'
        )
        try:
            action = int(input(menu_points))
            print(f'Вы выбрали: {action}')

            if action == 1:
                display_all()
            elif action == 2:
                create_contact()
            elif action == 3:
                find_one_contact()
            elif action == 4:
                update_contact()
            elif action == 5:
                remove_contact()
            elif action == 0:
                print('\nЗавершение программы\n')
                in_menu = False
            else:
                print(f'Некорректный ввод! Введите цифру соответствующую пункту меню')

        except ValueError:
            print(f'Некорректный ввод! Введите цифру соответствующую пункту меню')


if __name__ == '__main__':
    menu()
