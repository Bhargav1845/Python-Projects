import random

choices = ["rock", "paper", "scissors"]

while True:  
    user = input("Choose Rock, Paper, or Scissors: ").lower()
    if user in choices:
        break
    print("Invalid choice! Please choose Rock, Paper, or Scissors.")

com = random.choice(choices)

print(f"\nYou chose: {user.capitalize()}")
print(f"Computer chose: {com.capitalize()}")

if user == com:
    print("It's a tie!")
elif (user == "rock" and com == "scissors") or (user == "paper" and com == "rock") or (user == "scissors" and com == "paper"):
    print("You won!")
else:
    print("You lost!")