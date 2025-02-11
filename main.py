from register import *
from bank import *

print('''
*****************************************************

      Welcome to the Bank Management System

*****************************************************
''')

print('''
-----------------------------------------------------
| Choose the Given options:                          |
-----------------------------------------------------
| 1. Sign up                                         |
| 2. Sign in                                         |
| 3. Exit                                            |
-----------------------------------------------------
''')
status = False
while True:
    try:
        register = int(input("-> "))
        if register == 1 or register == 2:
            if register ==1 :
                SignUp()
            elif register == 2:
              user = SignIn()
              status = True
              break
        else:
            print("Please Enter a valid option")
            break
    except ValueError:
        print("Invalid input! Please enter a number")

account_no = db_query(f"SELECT account_no FROM customers WHERE username = '{user}';")
while status:
    print(f"Welcome {user.capitalize()} ! Choose Your Banking Services")
    try:
        facility = int(input("1. Balance Enquiry\n"
                                "2. Cash Deposite\n"
                                "3. Cash Withdraw\n"
                                "4. Fund Transfer\n"))

        if facility >= 1 and facility <= 4:
            if facility == 1:
                bobj = Bank(user, account_no[0][0])
                bobj.balanceenquiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter the amount you want to deposite :"))
                        bobj = Bank(user, account_no[0][0])
                        bobj.deposite(amount)
                        mydb.commit()
                        status = False
                        break
                    except ValueError:
                        print("Invalid input! Please enter a number")
                        continue
            elif facility == 3:
                while True:
                    try:
                        withdraw = int(input("Enter the amount you want to withdraw :"))
                        bobj = Bank(user, account_no[0][0])
                        bobj.withdraw(withdraw)
                        mydb.commit()
                        status = False
                        break
                    except ValueError:
                        print("Invalid input! Please enter a number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receiver = int(input("Enter Reciever Account Number :"))
                        amount = int(input("Enter Amount to transfer :"))
                        bobj = Bank(user, account_no[0][0])
                        bobj.fund_transfer(receiver, amount)
                        mydb.commit()
                        status = False
                        break
                    except ValueError:
                        print("Invalid input! Please enter a number")
                        continue
        else:
            print("Please Enter a valid option")
            continue

    except ValueError:
        print("Invalid input! Please enter a number")
        continue

