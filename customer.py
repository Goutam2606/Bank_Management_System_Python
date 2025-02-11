from database import *

class customer:
    def __init__(self,username, password, name, age, city, account_no):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_no = account_no

    def createuser(self):
        db_query(f"INSERT INTO customers VALUES ('{self.__username}', '{self.__password}', '{self.__name}', '{self.__age}', '{self.__city}', 0 , '{self.__account_no}', 1);")
        mydb.commit()
