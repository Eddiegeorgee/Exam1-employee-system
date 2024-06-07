# Create a program that provides the following options:
# Enter your choice 
# 1) Add new employee
# 2) Print all employees 
# 3) Delete by age
# 4) Update salary by name
# 5) End the program

employees = []

while True:
    print('''Enter your choice:
    1- Add new employee
    2- Print all employees
    3- Delete employee by age
    4- Update salary by employee name
    5- End the program''')
    choice = input("Choose the option: ")

    if choice == '1':
        name = input("Enter name: ").strip().capitalize()
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        employees.append({"name": name, "age": age, "salary": salary})
        print(f"Employee {name} added successfully.")
    elif choice == '2':
        if not employees:
            print("No employees to display.")
        else:
            for emp in employees:
                print(f"Name: {emp['name']}, Age: {emp['age']}, Salary: {emp['salary']}")
    elif choice == '3':
        age = int(input("Enter employee age to delete: "))
        employees = [emp for emp in employees if emp['age'] != age]
        print(f"Employees with age {age} deleted successfully.")
    elif choice == '4':
        name = input("Enter employee name to update the salary: ")
        new_salary = float(input("Enter new salary: "))
        for emp in employees:
            if emp['name'] == name:
                emp['salary'] = new_salary
                print(f"Salary updated for {name}.")
                break
        else:
            print(f"No employee found with name {name}.")
    elif choice == '5':
        print("Ending the program.")
        break
    else:
        print("Invalid choice. Please try again.")