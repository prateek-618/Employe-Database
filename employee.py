def check_hr(id):
    flag = False
    file = open("hr.txt", 'r')
    hr = file.readlines()
    for i in hr:
        j = i.split(',')
        if id == j[0]:
            flag = True
    return flag


def view_details(id):
    file = open("employee.txt", 'r')
    emp = file.readlines()
    for i in emp:
        j = i.split(',')
        if id == j[0]:
            return i
    else:
        return "Employee doesn't exist"


def view_employee(designation):
    file = open('employee.txt', 'r')
    emp = file.readlines()
    for i in emp:
        j = i.split(',')
        if designation == j[3]:
            print(i)
    return 0


def view_hr():
    file1 = open('hr.txt', 'r')
    file2 = open('employee.txt', 'r')
    hr = file1.readlines()
    emp = file2.readlines()
    for i in hr:
        for j in emp:
            k = i.split(',')
            l = j.split(',')
            if k[0] == l[0]:
                print(k[1] + ',' + l[1] + ',' + k[2])
                continue
    return 0


_name_ == '_main_'
id = input("Enter the id again: ")
if check_hr(id):
    while 1:
        print('enter 1 to view details\nenter 2 to view all employees\nenter q to exit')
        c = input("Enter your choice: ")
        if c == '1':
            print(view_details(id))
        elif c == '2':
            designation = input("Enter designation: ")
            view_employee(designation)
        elif c == 'q':
            break
else:
    while 1:
        print('enter 1 to view details\nenter 2 to view all HR names\nenter q to exit')
        c = input("Enter your choice: ")
        if c == '1':
            print(view_details(id))
        elif c == '2':
            view_hr()
        elif c == 'q':
            break