# Хранит информацию

from ast import Return


phone_numbers = {'Person_1': '111111',
                 'Person_2': '22222',
                 'Person_3': '333333',
}


def add_data(string_1, string_2):
    global phone_numbers
    phone_numbers[string_1] = string_2
    return string_1, string_2
    
def view_data(dictionary):
    global phone_numbers
    print(phone_numbers)
    
def remove_data(string_1):
    global phone_numbers
    del phone_numbers[string_1]
    print(phone_numbers)
    
def find_contact(string_1):
    global phone_numbers
    user_contact = string_1 + ": " + phone_numbers[string_1]
    # print(user_contact)
    return user_contact
    
# view_data(phone_numbers)

# add_data('Person_4', '444444')

# view_data(phone_numbers)

# remove_data('Person_1')

# view_data(phone_numbers)

find_contact('Person_2')    

    


