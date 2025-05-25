class Programmer:
    company = "Google"

    def __init__(self, name, salary, post):
        self.name = name 
        self.salary = salary
        self.post = post

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Post: {self.post}")
        print(f"Salary: ₹{self.salary}k")
        print(f"Company: {self.company}")
        print("--------------------")

p1 = Programmer("Bhargav", 500, "TL")
p2 = Programmer("Harry", 250, "HR")

p1.show_details()
p2.show_details()