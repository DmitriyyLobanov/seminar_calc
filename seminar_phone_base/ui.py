def get_what_do_it():
    while True:
        number = int(input("Выберите действие:\n 1 - Записать новый контакт;\n"
                    + "2 - Просмотреть список контактов;\n"
                    + "3 - Вывести информацию контакта;\n"
                    + "4 - Удалить контакт\n"
                    + "5 - Выйти из справочника\n"
                    + "Введите номер: "))
        if not number in [1, 2, 3, 4, 5]:
            number = int(input("Ошибка! Выберите действие.\n"
                    + "1 - Записать новый контакт;\n"
                    + "2 - Просмотреть список контактов;\n"
                    + "3 - Вывести информацию контакта;\n"
                    + "4 - Удалить контакт\n"
                    + "5 - Выйти из справочника\n"
                    + "Введите номер: "))
        if number == 5:
            break
    return number

def get_name():
    name = input('Введите ФИО/Имя/Никнейм: ')
    return name

def get_callnumber():
    callnumber = input('Введите номер телефона: ')
    return callnumber

def get_status():
    status_number = int(input("Кем вам приходится?" 
                        + "1 - Друзья;\n 2 - Родственники;\n"
                        + "3 - Коллеги;\n 4 - Прочее"
                        + "Введите номер: "))
    return status_number

def get_again():
    again = int(input("Хотите еще совершить действия с телефонным справочником? 1 - Да, 2 - Нет. Введите номер: "))
    if again == 1:
        get_what_do_it()
    else:
        exit()

def get_write(name, callnumber, status):
    call_list = [name, callnumber, status]
    return call_list