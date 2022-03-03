# Управляет всеми модулями

import view
import data


def check_command():
    user_command = view.hello_user()
    if user_command == 'a':
        user_name = view.view_data_add_name()[0]
        user_phone = view.view_data_add_phone()[1]
        return data.add_data(user_name, user_phone)
    elif user_command == 'd':
        data.remove_data(input(f'Введите имя пользователя, которого хотите удалить: '))
        view.view_data_remove()
    elif user_command == 'f':
        data.find_contact(input(f'Введите имя пользователя, которого Вы хотите найти: '))
        view.view_data_find
    else:
        print('Пожалуйста, введите буквы из меню')