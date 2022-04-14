# Модуль присвоения идентификатора добавленному пользователю.


def assign_id(data):
    id = int(sum(1 for line in open('seminar_phone_base\\log.json'))) + 1
    data.insert(0, id)
    return tuple(data)


