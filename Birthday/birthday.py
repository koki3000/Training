from datetime import datetime, timedelta

birthday = {
    'Kasia':'01-01-2023',
    'Jan':'27-10-1990',
    'Pankracy':'05-07-1967'
}

menu = '''
    What you want to do?
    1 - check birthdays
    0 - close the program
'''

print(menu)
today = datetime.now()
action = input('Input action number:')
while True:
    

    if action == '1':
        for person in birthday:
            birth_day = datetime.strptime(birthday[person], '%d-%m-%Y')
            birth_day = birth_day.replace(year = today.year)
            print(birth_day)
            delta = birth_day - today
            if delta.days < 0:
                birth_day = birth_day.replace(year = today.year + 1)
                delta = birth_day - today
            print(f'{person} {birthday[person]}, days to birthday: {delta.days}')
        break
    elif action == '0':
        break
    else:
        action = input('Input proper action number:')