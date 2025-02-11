import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="Goutam@123",
    database="bank"
)

cursor = mydb.cursor()
def creatcustomertable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers(
        username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        age INTEGER NOT NULL,
        city VARCHAR(20) NOT NULL,
        balance INTEGER NOT NULL DEFAULT 0,
        account_no INTEGER NOT NULL,
        status BOOLEAN NOT NULL DEFAULT 1
        )'''
)
    mydb.commit()
    cursor.close()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

if __name__ == '__main__':
    creatcustomertable()
    print('Table created successfully')