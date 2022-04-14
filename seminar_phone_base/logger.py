# Модуль логирования данных

import json
import xml


def log_json(data):
    with open('seminar_phone_base\\log.json', 'a') as file:
        res = str(data)
        file.write(f'{res}\n')

def log_xml(data):
    res  = ""
    for i in data:
        res += f'{i}\n'
    with open('seminar_phone_base\\log.xml', 'a') as file:
        #res = str(data)
        file.write(f'{res}\n')
   


