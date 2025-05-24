tasks = []

while True:
    task = input("Enter a task (or press 'e' to exit): ")

    if task.lower() == "e":
        break  

    tasks.append(task) 

print("\nTO-DO LIST:")
for t in tasks:
    print("~ " + t)
