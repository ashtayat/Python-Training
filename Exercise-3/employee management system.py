class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def __str__(self):
        return f"{super().__str__()}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"{super().__str__()}, Programming Language: {self.programming_language}"

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee)

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary

# Create a company instance
company = Company()

# User input loop
while True:
    print("\n1. Add a new employee")
    print("2. Display employees")
    print("3. Calculate total salary")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter employee's name: ")
        age = int(input("Enter employee's age: "))
        salary = float(input("Enter employee's salary: "))
        employee_type = input("Enter employee type (Manager/Developer): ")

        if employee_type.lower() == 'manager':
            department = input("Enter department: ")
            company.add_employee(Manager(name, age, salary, department))
        elif employee_type.lower() == 'developer':
            programming_language = input("Enter programming language: ")
            company.add_employee(Developer(name, age, salary, programming_language))
        else:
            print("Invalid employee type. Please enter 'Manager' or 'Developer'.")
    elif choice == '2':
        company.display_employees()
    elif choice == '3':
        print(f"Total salary of all employees: {company.calculate_total_salary()}")
    elif choice == '4':
        print("Thank you for using Estarta Solutions Employee Management System.Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")