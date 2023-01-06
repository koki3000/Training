from datetime import datetime
import json

try:
    with open('calendar.json', 'r+') as file:
        birthday = json.load(file)
except:
    birthday = {}

menu = '''
    What you want to do?
    1 - check birthdays
    2 - add person
    0 - close the program
'''

print(menu)
today = datetime.now()
while True:
    
    action = input('Input action number:')
    if action == '1':
        for person, date in birthday.items():
            birth_day = datetime.strptime(date, '%d-%m-%Y')
            birth_day = birth_day.replace(year = today.year)
            delta = birth_day - today
            if delta.days < 0:
                birth_day = birth_day.replace(year = today.year + 1)
                delta = birth_day - today
            print(f'{person} {date}, days to birthday: {delta.days}')
    elif action == '0':
        with open('calendar.json', 'w+') as file:
            json.dump(birthday, file)
        break
    elif action == '2':
        new_name = input('Input name:')
        new_date = input('Input date in format dd-mm-yyyy:')
        birthday[new_name] = new_date
    else:
        action = input('Input proper action number:')