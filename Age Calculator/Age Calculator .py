from datetime import date

current_day = 23
current_month = 3
current_year = 2025

birth_day = int(input("Enter your birth day : "))
birth_month = int(input("Enter your birth month : "))
birth_year = int(input("Enter your birth year : "))

age = current_year - birth_year

if (birth_month , birth_day) > (current_month , current_day):
    age -= 1

print(age)