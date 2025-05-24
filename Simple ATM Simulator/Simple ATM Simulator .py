balance = 0

while True:
    choice = int(input("1. Deposit Money \n2. Withdraw Money \n3. Check Balance \n4. Exit \n"))

    if choice == 1:
        amt_d = float(input("Enter the Amount you want to deposit : "))
        balance += amt_d
        print(f"₹{amt_d} deposited successfully!\n")

    elif choice == 2:
        amt_w = float(input("Enter the Amount you want to withdraw : "))
        if amt_w <= balance:
            balance -= amt_w
            print(f"₹{amt_w} withdrawn successfully!\n")
        else:
            print("Insufficient balance! Withdrawal failed.\n")

    elif choice == 3:
        print(f"Your current balance is: ₹{balance}\n")

    elif choice == 4:
        print("Thanks for using this ATM. Goodbye!")
        break

    else:
        print("Invalid Input. Please try again.\n")
