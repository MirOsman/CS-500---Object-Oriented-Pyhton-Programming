def menu():
    print("e - Enter a new employee's information")
    print('a - Display all employees information ')
    print("d - Display an employee's information")
    print('q - Quit')
    choice = input()
    return choice

def new_emp(emps_list):
    employee = list()
    
    print("Please provide the name, ID, department number, and age of an employee (space separated).")
    employee = input("Entry: ").split(' ')
    emps_list.append(employee)

def disp_all(emps_list):
    for i in range(len(emps_list)):
        print(f"Employee_{i+1}: {', '.join(emps_list[i])}")

def disp_emp(emps_list):
    name = input("Enter the name of an employee: ")
    for i in range(len(emps_list)):
        if emps_list[i][0] == name:
            print(', '.join(emps_list[i]))
        else:
            new = input('Enter a new name (y/n)? ')
            if new in ['y', 'Y']:
                disp_emp(emps_list)
employees = list()

while True:
    choice = menu()
    if choice == 'e':
        new_emp(employees)

    elif choice == 'a':
        disp_all(employees)

    elif choice == 'd':
        disp_emp(employees)

    elif choice == 'q':
        break
    else:
        print('Invalid choice.')

