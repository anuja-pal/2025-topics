class Worker:
    def __init__(self, name, id, department, hourly_salary):
        self.name = name
        self.id = id
        self.department = department
        self.hourly_salary = hourly_salary

    def display_profile(self):
        print("===========================================")
        print(f"Employee name: {self.name}")
        print(f"Employee ID: {self.id}")
        print(f"Department: {self.department}")
        print(f"Hourly Salary: {self.hourly_salary} euros")
        print("===========================================")

    def calculate_salary(self, hours_worked):
        print(f"Your total salary is: {self.hourly_salary}*{hours_worked} euros.")


class Manager(Worker):
    def __init__(self, name, id, department, hourly_salary, hourly_bonus):
        super().__init__(name, id, department, hourly_salary)
        self.hourly_bonus = hourly_bonus

    def calculate_salary(self,hours_worked):
        print(f"Your total salary inclusive of bonus is: {(self.hourly_salary+self.hourly_bonus)*hours_worked}")


    