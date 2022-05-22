import csv
import sys
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from statistics import mean
import matplotlib.pyplot as plt
import re

get = open("Customer.txt", "r+")
temp = get.readlines()
details = []
for i in range(len(temp)):
    details.append(temp[i])
    
get1 = open("index.txt", "r+")
temp1 = get1.readlines()
details1 = []
for i in range(len(temp1)):
    details1.append(temp1[i])   
    
file = open("Admin.txt", "r+")
file1 = file.readlines()
ls = []
for i in range(len(file1)):
    ls.append(file1[i])
 
ge = open("add.txt", "r+")
tp = ge.readlines()
di = []
for i in range(len(tp)):
    di.append(tp[i])

def Signup():
            username=input("Enter Username : ")
            for o in range(len(details)):
                if details[o].startswith(username):
                    print("User name already exists")
                    exit()
            password=input("Enter Password : ")
            age=input("Enter age : ")
            Aadhar=input("Enter Aadhar Number : ")
            phone=phvalidate()
            dl=dlvalidate()
            ct=len(details)+1
            cid="CUS"+str(ct)
            outfile = open('INV.csv', 'a', newline='')
            w=csv.writer(outfile) 
            w.writerow([cid, username, password, age, Aadhar, phone,dl])
            final = f"\n{cid}|{username}|{password}|{age}|{Aadhar}|{phone}|{dl}|"
            details.append(final)
            fout = open("Customer.txt", "r+")
            for j in range(len(details)):
                op = f"{details[j]}"
                fout.write(op)
            fout.close()
            outfile.close()
            print("------------------------------")
            print("Your Unique User id is : ",cid)
            print("------------------------------")
            print("--NOTE:Remember Your User ID--")
            print("------------------------------")
            vsort()
            main()
            
def dlvalidate():
    dl=input("Enter Driving License Number : ")
    result =dl.startswith("DL")
    while not result:
        print("Note : DL Number must start with DL")
        dl=input("Enter Driving License Number : ")
        result =dl.startswith("DL")
    return dl

def phvalidate():
    ph=input("Enter Phone Number : ")
    pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    result= pattern.match(ph)
    while not result:
        print("Phone number is not in a valid format")
        ph=input("Enter Phone Number : ")
        pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        result= pattern.match(ph)
    return ph
                     
def login():
    get = open("Customer.txt", "r+")
    temp = get.readlines()
    details = []
    for i in range(len(temp)):
        details.append(temp[i])
    userid=input("Enter Userid: ").upper()
    data = []
    for p in range(len(details)):
        if details[p].startswith(userid):
            data = details[p].split("|") 
    password =input("Enter Password : ")
    count = 3
    while password != data[2]:
        print("Wrong password")
        print(f"You have {count} attempts left")
        password = input("Enter the password :")
        if count == 1:
            print("Wrong Password,Come Back when you remember it")
            exit()
        count -= 1
    customer_menu(userid)
        
def customer_menu(userid):
    get = open("Customer.txt", "r+")
    temp = get.readlines()
    details = []
    for i in range(len(temp)):
        details.append(temp[i])
    data = []
    for p in range(len(details)):
        if details[p].startswith(userid):
            data = details[p].split("|")
    name = data[1].upper()
    print(f"Welcome {name}")
    print("------------------------------------------------------------------")
    print(f"{name} , Choose an Option")
    print("1.View My Profile \n2.Update Profile\n3.Get Quotation\n4.View and Book Car\n5.Exit")
    print("------------------------------------------------------------------")
    choice1=input("Enter Your Option\n")
    if choice1=="1":
        viewmyprof(userid)
    elif choice1=="2":
        update()
    elif choice1=="3":
        quotation()
    elif choice1=="4":
        viewandbookcar(userid)
    elif choice1=="5":
        sys.exit("You Pressed Exit")
    else:
        print("Enter valid option....")
        customer_menu(userid)
            
def update():
    uid= input("Enter the USER-ID:").upper()
    get = open("Customer.txt", "r+")
    temp = get.readlines()
    details = []
    for i in range(len(temp)):
        details.append(temp[i])
    print("------------------------------------------------------------------")
    for i in range(len(details)):
                if details[i].startswith(uid):
                    data = details[i].split("|")
                    print(f"Customer  Name is {data[1]}")
                    data[1] = input("Enter the Name: ")
                    data[2] = input("Enter the password: ")
                    data[3] = input("Enter the Age : ")
                    data[4] = input("Enter the Aadhar No: ")
                    data[5] = phvalidate()
                    data[6] = dlvalidate()
                    print("------------------------------------------------------------------")
                    vupdate = f"{uid}|{data[1]}|{data[2]}|{data[3]}|{data[4]}|{data[5]}|{data[6]}|\n"
                    for i in range(len(details)):
                        if details[i].startswith(uid):
                            details[i]=vupdate
                    fout = open("Customer.txt", "r+")
                    for j in range(len(details)):
                        op = f"{details[j]}"
                        fout.write(op)
                    fout.close()
    customer_menu(uid)
               
def quotation():
    uid= input("Enter the USER-ID:").upper()
    print("------------------------------------------------------------------")
    km=int(input("Enter the approximate number of kilometers you want to drive the car \n "))
    days=int(input("Enter the number of days you want to rent the car \n "))
    print("------------------------------------------------------------------")
    data=pd.read_csv("./training.csv")
    x = data.drop('PRICE', axis=1)
    y=data["PRICE"]
    new_data = pd.DataFrame()
    new_data['KM'] = [km]
    new_data['DAYS'] = [days]
    model=LinearRegression()
    model=model.fit(x,y)
    quoted_price=model.predict(new_data)[0]
    print("The Quoted price for the given inputs is ",quoted_price)
    print("------------------------------------------------------------------")
    customer_menu(uid)
                   
def vsort():
    get = open("Customer.txt", "r")
    get.seek(0)
    temp = get.readlines()
    v = []
    for i in range(len(temp)):
        if temp[i].startswith("CUS"):
            v.append(temp[i])
    fout = open("Customer.txt", "w")
    v.sort()
    for j in range(len(v)):
        final = f"{v[j]}"
        fout.write(final)
    fout.close()
    fin1 = open("Customer.txt","r")
    fin2 = open("index.txt","w")
    fin1.seek(0)
    details = fin1.readlines()
    for i in range(len(details)):
        data = details[i].split("|")
        fin2.write(f"{i}|{data[0]}|\n")
    fin1.close()
    fin2.close()
    get.close()
    
                 
                    
def remove_customer(cusid):
    get = open("Customer.txt","r")
    details = get.readlines()
    for i in range(len(details)):
        if details[i].startswith(cusid):
            clear = ""
            details[i] = clear
            fout = open("Customer.txt", "r+")
            for j in range(len(details)):
                op = f"{details[j]}"
                fout.write(op)
            fout.close()
    vsort()
    get.close()               
   
def viewmyprof(userid):
    get = open("Customer.txt", "r+")
    temp = get.readlines()
    details = []
    for i in range(len(temp)):
        details.append(temp[i])
    for z in range(len(details)):
            if details[z].startswith(userid):
                data = details[z]
                data = data.split("|")
    user_id=data[0]
    name = data[1]
    age = data[3]
    aadhar = data[4]
    phone = data[5]
    dl=data[6]
    print(f"Hello {name} \n")
    print("------------------------------------------------------------------")
    print(f"User_ID : {user_id}\nAge : {age} \nAadhar Number : {aadhar}\nPhone Number : {phone}\nDriving License No:{dl}")
    print("------------------------------------------------------------------")
    customer_menu(user_id)
    
def viewandbookcar(userid):
    print(userid)
    data=pd.read_csv("./Add.csv")
    print(data)
    print("------------------------------------------------------------------")
    print("Enter the id of the car you want to book")
    print("------------------------------------------------------------------")
    car_id=input().upper()
    get = open("add.txt","r+")
    details = get.readlines()
    for i in range(len(details)):
        if details[i].startswith(car_id):
            data = details[i]
            data = data.split(",")
    if data[9]=="true":
        print("Already Booked")
        customer_menu(userid)
    else:
        fout1 = open("add.txt", "r+")
        details = fout1.readlines()
        for i in range(len(details)):
            if details[i].startswith(car_id):
                data = details[i]
                data = data.split(",")
        car_id=data[0]
        car_name=data[1]
        car_model=data[2]
        car_seats=data[3]
        car_color=data[4]
        car_mil=data[5]
        car_year=data[6]
        car_fuel=data[7]
        car_type=data[8]
        flag="true"
        vupdate = f"{car_id},{car_name},{car_model},{car_seats},{car_color},{car_mil},{car_year},{car_fuel},{car_type},{flag},\n"
        for i in range(len(details)):
            if details[i].startswith(car_id):
                details[i]=vupdate
        fout = open("add.txt", "r+")
        for j in range(len(details)):
            op = f"{details[j]}"
            fout.write(op)
        fout.close()
        print("------------------------------------------------------------------")
        print("You have Successfully booked a Car")
        print("------------------------------------------------------------------")
        log=open("logs.txt","a")
        logg=f"{userid}|{car_id}|\n"
        log.write(logg)
        log.close()
        customer_menu(userid)
    
def login_admin(username,password):
    data = []
    for p in range(len(ls)):
        if ls[p].startswith(username):
            data = ls[p].split("|") 
    count = 3
    while password != data[1]:
        print("Wrong password")
        print(f"You have {count} attempts left")
        password = input("Enter the password :")
        if count == 0:
            print("Wrong Password,Come Back when you remember it")
            exit()
        count -= 1
    name = data[0]
    admin_menu(name)  

def admin_menu(name):
    print(f"Welcome {name}")
    print("------------------------------------------------------------------")
    print("what would u like to to ")
    print('1 Add Vehicle to Inventory')
    print('2 Delete Vehicle from Inventory')
    print('3 View Current Inventory')
    print('4 Update Vehicle in Inventory')
    print('5 View Logs') 
    print('6 Analyse Yearly Data')
    print('7 Quit')
    print("------------------------------------------------------------------")
    userInput=input('Please choose from one of the above options: ') 
    print("------------------------------------------------------------------")
    if userInput=="1":
        add(name)
    elif userInput=="2":
        car_id = input('Please enter the number associated with the vehicle to be removed: ')
        remove_car(car_id.upper(),name)
        print("This vehicle has been removed an the updated vehicle inventory is ")
        display(name)
    elif userInput=="3":
            display(name)  
    elif userInput=="4":
        update_car(name)
    elif userInput=="5":
        view_logs(name)
    elif userInput == '6':
        analyse(name)
    elif userInput == '7':
        exit()
    else:
        print('This is an invalid input. Please try again.')
        admin_menu(name)

def add(name): 
    print("------------------------------------------------------------------")
    print("Adding a Car to Inventory")
    print("------------------------------------------------------------------")
    fi=open("add.txt","r+")
    z=len(di)+1
    car_id="CAR"+str(z)
    car_name=input("Enter car make : ")
    car_model=input("Enter car model:")
    seats=input("Enter number of seats:")
    color = input('Enter vehicle color: ')
    mileage = int(input('Enter vehicle mileage: '))
    year =int(input('Enter vehicle year: '))
    fuel_type=(input('Enter vehicle fuel_type: '))
    car_type =(input('Enter vehicle car_type: '))
    List=[car_id,car_name,car_model,seats,color,mileage,year,fuel_type,car_type]
    print("-----------------------------------------------------------------")
    flag="false"
    re=f"{car_id},{car_name},{car_model},{seats},{color},{mileage},{year},{fuel_type},{car_type},{flag},\n" 
    di.append(re)
    gout=open("add.txt", "r+")
    for i in range(len(di)):
        yo=f"{di[i]}"
        gout.write(yo)
    gout.close()
    with open('Add.csv', 'a') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(List)
        f_object.close()
    admin_menu(name) 

def remove_car(car_id,name):
    ge1 = open("add.txt","r")
    de = ge1.readlines()
    data=pd.read_csv("./Add.csv")
    index=data.index
    ind=index[data["CAR_ID"]==car_id].tolist()[0]
    data.drop(ind,inplace=True,axis=0)
    data.to_csv('./Add.csv',index=False)
    for i in range(len(de)):
        if de[i].startswith(car_id):
            clear = ""
            de[i] = clear
            fout = open("add.txt", "w")
            for j in range(len(de)):
                op = f"{de[j]}"
                fout.write(op)
            fout.close()
    vsort1()
    ge1.close()  
    

def vsort1():
    get = open("add.txt", "r")
    get.seek(0)
    temp = get.readlines()
    v = []
    for i in range(len(temp)):
        if temp[i].startswith("CAR"):
            v.append(temp[i])
    fout = open("add.txt", "w")
    v.sort()
    for j in range(len(v)):
        final = f"{v[j]}"
        fout.write(final)
    fout.close()
    fin1 = open("add.txt","r")
    fin2 = open("index1.txt","w")
    fin1.seek(0)
    details = fin1.readlines()
    for i in range(len(details)):
        data = details[i].split(",")
        fin2.write(f"{i}|{data[0]}|\n")
    fin1.close()
    fin2.close()
    get.close()
   
    
def display(name):
    print("------------------------------------------------------------------")
    data1=pd.read_csv("./Add.csv")
    print(data1)
    print("------------------------------------------------------------------")
    admin_menu(name) 
    
def update_car(name):
    ge2 = open("add.txt", "r+")
    tp1 = ge2.readlines()
    dt = []
    for i in range(len(tp1)):
        dt.append(tp1[i])
    car_id= input("Enter the CAR_ID:").upper()
    print("------------------------------------------------------------------")
    for i in range(len(dt)):
        if dt[i].startswith(car_id):
            data = dt[i].split(",")
            print("------------------------------------------------------------------")
            print(f"Car is of {data[1]} and model name is {data[2]}")
            print("------------------------------------------------------------------")
    data = pd.read_csv('./Add.csv')
    if (car_id in data['CAR_ID'].tolist()):
        index=data.index
        ind=index[data["CAR_ID"]==car_id].tolist()[0]
        make = input("Enter car make : ")
        model= input("Enter car model:")
        seats= input("Enter number of seats:")
        color= input('Enter vehicle color: ')
        mil =  input('Enter vehicle mileage: ')
        year = input('Enter vehicle year: ')
        fuel = input('Enter vehicle fuel_type:')
        type = input('Enter vehicle car_type: ')
        data.loc[ind,"Name"]=make
        data.loc[ind,"Model"]=model
        data.loc[ind,"Seats"]=seats
        data.loc[ind,"Color"]=color
        data.loc[ind,"Mileage"]=mil
        data.loc[ind,"YOM"]=year
        data.loc[ind,"Fuel Type"]=fuel
        data.loc[ind,"Car_type"]=type        
        data.to_csv("Add.csv",index=False)
    else:
        print("Car Not found")
        admin_menu(name)
        
    print("------------------------------------------------------------------")
    for i in range(len(dt)):
        if dt[i].startswith(car_id):
            data = dt[i].split(",")
            print("------------------------------------------------------------------")
            print("------------------------------------------------------------------")
            data[1] = make
            data[2] = model
            data[3] = seats
            data[4] = color
            data[5] = mil
            data[6] = year
            data[7] = fuel
            data[8] = type
            flag="false"
            print("------------------------------------------------------------------")
            vupdate = f"{car_id},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]},{data[7]},{data[8]},{flag},\n"
            for i in range(len(dt)):
                if dt[i].startswith(car_id):
                            dt[i]=vupdate
                pout = open("add.txt", "r+")
                for j in range(len(dt)):
                        o = f"{dt[j]}"
                        pout.write(o)
                pout.close()
    admin_menu(name) 
    
def analyse(name):
    data=pd.read_csv("./Yearlydata.csv")
    for i in data.index:
        row = data.iloc[i]
        print("Visualization for Customer: "+str(row['CusID']))
        row.drop("CusID", inplace=True)
        row.plot(kind='bar',color='red')
        plt.xlabel("Month")
        plt.ylabel("Number of cars rented")
        plt.title("Bar Graph Showing the number of cars rented by cutomer in each month")
        plt.show()
    admin_menu(name)
    

def view_logs(name):
    with open('logs.txt') as f:
        lines = f.read()
        print("------------------------------------------------------------------")
        print(lines)
        print("------------------------------------------------------------------")
    admin_menu(name)   
 
def admin_main():
    print("------------------------------------------------------------------")
    print("----------------------CAR RENTAL SYSYTEM--------------------------")
    print("-------------------------ADMIN PORTAL-----------------------------")
    print("------------------------------------------------------------------")
    print("---------------------Welcome to Dashboard-------------------------")
    print("------------------------------------------------------------------")
    username=input("Enter Username : ")
    password =input("Enter Password : ")
    print("------------------------------------------------------------------")
    login_admin(username,password)   
                 
def customer_main():
        print("------------------------------------------------------------------")
        print("----------------------CAR RENTAL SYSYTEM--------------------------")
        print("-----------------------CUSTOMER PORTAL----------------------------")
        print("------------------------------------------------------------------")
        print("Welcome to Dashboard")
        print("1.Login \n2.Signup")
        choice=input()
        if choice == "2":
            Signup()
        elif choice == "1":
            login()
        else:
            print("Enter Valid Option")
            exit()

def main():
    print("------------------------------------------------------------------")
    print("----------------------CAR RENTAL SYSYTEM--------------------------")
    print("------------------------------------------------------------------")
    print("----------------------Admin or Customer---------------------------")
    print("----------------A for Admin and C for Customer--------------------")
    print("------------------------Q for Quit--------------------------------")
    print("------------------------------------------------------------------")
    choice=input().upper()
    if choice=="A":
        admin_main()
    elif choice=="C":
        customer_main()
    elif choice=="Q":
         sys.exit("You Pressed Quit")  
    else:
        print("Enter a Valid Option\nTry again")
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        main()
    
main()