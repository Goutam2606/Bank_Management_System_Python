#user registration sign in sign up
from database import *
import random
from customer import customer
from bank import Bank

def SignUp():
    username = input("Create Username :")
    temp = db_query(f"SELECT * FROM customers WHERE username = '{username}';")
    if temp:
        print("Username already exists")
        return SignUp()

    print('Username is Available please Proceed')
    password = input("Enter Your Password :")
    name = input("Enter Your Name :")
    age = input("Enter Your Age :")
    city = input("Enter Your City :")

    while True:
        try:
            account_no = random.randint(10000000,99999999)
            temp = db_query(f"SELECT account_no FROM customers WHERE account_no = '{account_no}';")
            if temp:
                continue
            else:
                print(f"Your Account Number is : {account_no}")
                break

        except ValueError:
            print("Invalid input! Please enter a number")

    cobj = customer(username, password, name, age, city, account_no)
    cobj.createuser()
    bobj = Bank(username, account_no)
    bobj.create_transaction_table()

def SignIn():
    username = input("Enter Your Username :")
    temp = db_query(f"SELECT username FROM customers WHERE username ='{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Your Password :")
            temp = db_query(f"SELECT password FROM customers WHERE username ='{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("Sign In Successful")
                return username
            else:
                print("Incorrect Password")
                continue

    else:
        print("Username does not exist")
        SignIn()