import datetime

while True:
    birthday = input("Enter your birthday in format (YYYY-MM-DD): ")

    try:
        user_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        break  
    except ValueError:
        print("Invalid format! Please enter in YYYY-MM-DD format.")

user_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")

current_date = datetime.datetime.now()

user_date = user_date.replace(year=current_date.year)

if user_date < current_date:
    user_date = user_date.replace(year=current_date.year + 1)

days_left = (user_date - current_date).days

print(f"Your next birthday is in {days_left} days!")