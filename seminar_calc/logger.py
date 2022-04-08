from datetime import datetime as dt

def log_operations(data):
    time =dt.now().strftime('%H:%M')
    with open('seminar_calc/seminar_calc/log.txt', 'a') as file:
        file.write('{} operation {}\n'
                    .format(time, data))