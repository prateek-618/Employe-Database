#!/usr/bin/env python
# coding: utf-8

# In[1]:


def employee(id,pwd):
    if(search_hr(id)==False):
        print('welcome',pwd)
        while(1):
            print("\n 1-Enter 1 to view own details\n2-Enter 2 to view all HR names\n3-quit")
            c=int(input("enter ur choice:"))
            if c==1:
                print(showemp(id))
            elif c==2:
                a=open("hr.txt",'r')
                b=open("employee.txt",'r')
                hr=a.readlines()
                emp=b.readlines()
                for i in hr:
                    for j in emp:
                        k=i.split(',')
                        l=j.split(',')
                        if k[0]==l[0]:
                            print(k[1]+','+l[1]+','+k[2])
                            continue
               
                a.close()
                b.close()
            else:
                break
    elif(search_hr(id)==True):
        print('welcome',pwd)
        while(1):
            print("\n 1-Enter 1 to view own details\n2-Enter 2 to view all employees\n3-quit")
            c=int(input("enter ur choice:"))
            if c==1:
                print(showemp(id))
            elif c==2:
                a=open("employee.txt",'r')
                b=a.readlines()
                print(b)
                a.close()
            else:
                break
                
            
                
def search_hr(emp_id):
    file = open("hr.txt", "r")
    hr = file.readlines()
    for i in hr:
        j = i.split(',')
        if emp_id == j[0]:
            return True
    else:
        return False   

def showemp(emp_id):
    file = open("employee.txt", "r")
    employee = file.readlines()
    for i in employee:
        j = i.split(',')
        if emp_id == j[0]:
            return i
        
    else:
        return "not found"    


# In[2]:


print("Welcome to Employee System")
id = input("Please Enter Login id:  ")
pwd = input("Please Enter Password:  ")
file = open("login.txt", "r")
a = file.readlines()
for i in a:
    b = i.split()
    if id == b[0] and pwd == b[1]:
        employee(id,pwd)
        break
else:
    print("invalid id and password")
    

