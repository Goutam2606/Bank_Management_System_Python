# Bank
from  database import *
import datetime
class Bank:
    def __init__(self, username, account_no):
        self.__username = username
        self.__account_no = account_no
        self.create_transaction_table

    def create_transaction_table(self):
        temp = db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction"
                        f"( timedate VARCHAR(30),"
                        f"account_no INTEGER,"
                        f"remarks VARCHAR(50),"
                        f"amount INTEGER)")

    def balanceenquiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        print(f"Current Balance is : {temp[0][0]}")

    def deposite(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        test = amount + temp[0][0]
        db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
        self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_no}',"
                 f"'Amount Deposited',"
                 f"'{amount}'"
                 f")"
                 )
        print(f"{self.__username} Amount is Sucessfully Deposited into Your Account {self.__account_no}")

    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposite Money")
        else:
            test = temp[0][0] - amount
            db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
            self.balanceenquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_no}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")"
                     )
        print(f"{self.__username} Amount is Sucessfully Withdraw from Your Account {self.__account_no}")

    def fund_transfer(self, receive, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")

        if not temp:
            print("Invalid Account Number")
            return

        sender_balance = temp[0][0]

        temp2 = db_query(f"SELECT balance FROM customers WHERE account_no = '{receive}';")

        if not temp2:
            print("Invalid Account Number")
            return

        receiver_balance = temp2[0][0]

        if amount > sender_balance:
            print("Insufficient Balance Please Deposite Money")
            return

        new_sender_balance = sender_balance - amount
        db_query(f"UPDATE customers SET balance = '{new_sender_balance}' WHERE username = '{self.__username}';")

        new_reciever_balance = receiver_balance + amount
        db_query(f"UPDATE customers SET balance = '{new_reciever_balance}' WHERE account_no = '{receive}';")

        receive_transaction = db_query(f"SELECT username FROM customers WHERE account_no = '{receive}';")
        receive_username = receive_transaction[0][0]
        db_query(f"INSERT INTO {receive_username}_transaction VALUES ("
                    f"'{datetime.datetime.now()}',"
                     f"'{self.__account_no}',"
                     f"'Transfer {amount}₹ to {receive}',"
                     f"'{amount}'"
                     f")"
)

        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                    f"'{datetime.datetime.now()}',"
                     f"'{self.__account_no}',"
                     f"'Amount Transfer -> {receive}',"
                     f"'{amount}'"
                     f")"
                     )
        print(f"{amount} is Sucessfully Transfer to Account No. {receive}")
        self.balanceenquiry()
