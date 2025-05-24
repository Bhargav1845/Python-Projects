def add_expense():
    amount = float(input("Enter Amount : $"))
    description = input("Enter Description : ")

    with open("expense.txt", "a") as f:
        f.write(f"{amount}  -  {description}\n") 

def view_expense():
    with open("expense.txt", "r") as f:
        print(f.read()) 

def total_expense():
    total = 0
    with open("expense.txt", "r") as file:
        for line in file:
            amount = float(line.split("-")[0].strip())
            total += amount
    print(f"\nTotal money spent: ${total}\n")

while True:

    ch = int(input("1. ADD Expense \n2. View Expenses \n3. Total Expenses \n4. Exit \n"))

    if ch == 1:
        add_expense()
    elif ch == 2:
        view_expense()
    elif ch == 3:
        total_expense()
    elif ch == 4:
        print("Thank you for using Expense tracker !")
        break
    else:
        print("Invalid Input")
