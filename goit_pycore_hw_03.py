# Завдання 1

from datetime import datetime

def get_days_from_today(date):

    try:
        given_date = datetime.strptime(date, '%Y-%m-%d')
        
        today = datetime.today()
        
        difference = (today - given_date).days
        
        return difference
    except ValueError:
        print("Error: The date format should be 'YYYY-MM-DD'.")
        return None

result = get_days_from_today("2021-10-09")
print(result)


# Завдання 2

import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# Завдання 3

import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number.strip())
    
    if cleaned_number.startswith('+'):
        if cleaned_number.startswith('+38'):
            return cleaned_number
        else:
            cleaned_number = '+' + cleaned_number[1:]
    else:
        cleaned_number = '+38' + cleaned_number

    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Завдання 4

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:  
                congratulation_date += timedelta(days=2)  
            elif congratulation_date.weekday() == 6: 
                congratulation_date += timedelta(days=1)  

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1988.01.29"},
    {"name": "Bob Brown", "birthday": "1975.01.22"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
