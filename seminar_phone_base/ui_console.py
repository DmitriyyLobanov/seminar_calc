


def get_user_info():
    print('Добавление нового пользователя.')
    user_name = input('Введите имя: ')
    user_surname = input('Введите фамилию: ')
    user_birth_date = input('Укажите дату рождения:')
    user_phone_number = input('Укажите номер телефона: ')
    print('Добавление нового пользователя совершено.')
    print()
    return [user_name, user_surname, user_birth_date, user_phone_number]

def get_mode():
    mode = input('Выберите режим работы приложения:\n\
        (1 - режим добавления нового пользователя, 2 - режим поиска пользователя)\n')
    while is_int(mode) == False or mode not in ["1", "2"]:
        mode = input('Выберите режим работы приложения:\n\
            (1 - режим добавления нового пользователя, 2 - режим поиска пользователя)\n')
    else:
        return mode

def find_user():
    arg_str = input('Введите информацию для поиска пользователя: ')
    file = open('seminar_phone_base\\log.json').readlines()
    for i in file:
        if str(arg_str) in i:
            return print(f'{i}')
    return print('Совпадений не найдено.')



def is_int(arg):
    try:
        int(arg)
        return True
    except:
        return False
