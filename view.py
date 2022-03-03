# Отвечает за взаимодействие с пользователем

import data

def hello_user():
    user_command = input(f'Здравствуйте! Что бы вы хотели сделать?\nДобавить = a, удалить = d, найти = f\n')
    return user_command

def view_data_add_name():
    added_contact_name = input(f'Добавьте имя: ')
    print(f'Данные успешно добавлены: ', added_contact_name)
    return added_contact_name
    
def view_data_add_phone():
    added_contact_phone = input(f'Добавьте телефон: ')
    print(added_contact_phone)
    return added_contact_phone    

def view_data_remove(dictionary):
    print(f'Данные успешно удалены: {dictionary}')
    
def view_data_find(dictionary):
    dictionary = data.find_contact
    print(f'Искомый контакт: ', dictionary)