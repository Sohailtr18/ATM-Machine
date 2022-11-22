import time
import random
from datetime import datetime, timedelta
import mysql.connector
import sys
import os

sb_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your DB Pass",
    database="atm_machine_db"
)
mycursor = sb_db.cursor()

# # creating db
mycursor.execute("CREATE DATABASE IF NOT EXISTS atm_machine_db")
# # creating table
mycursor.execute("create table if not exists atm_machine_db (uid VARCHAR(30) NOT NULL PRIMARY KEY,password VARCHAR(30),FirstName VARCHAR(30),LastName VARCHAR(30),mobileno VARCHAR(10), Deposit INT,balance INT)")


class Atmachine():

    def register(self, uid, password, FirstName, LastName, mobileno, Deposit):
        sql = ("insert into atm_machine_db(uid,password,FirstName,LastName,mobileno,Deposit) values(%s,%s,%s,%s,%s,%s)")
        val = (uid, password, FirstName, LastName, mobileno, Deposit)
        mycursor.execute(sql, val)
        mycursor.execute("update atm_machine_db set balance = Deposit")
        sb_db.commit()
        print("Account Registered Successfully")

    def main_page(self):
        print('''\n\n1-Fast Cash \n2-Withdrawl \n3-Balance Enquiry \n4-Mini Statement \n5-Pin Change\n\n''')
        main_page_input = int(input("Choose the Number: "))
        if main_page_input == 1 or main_page_input == 2 or main_page_input == 3 or main_page_input == 4 or main_page_input == 5:
            if main_page_input == 1:
                print("Fast Withdrwal Amount Limit 10,000\n\n")
                fastcash_amount = int(input("Enter the Amount: "))
                if fastcash_amount > 10000:
                    print("\n\nFast Cash Not Available more than 10,000")
                elif fastcash_amount <= 10000:
                    mycursor.execute(
                        '''select balance FROM atm_machine_db WHERE uid=%s''', [(uid)])
                    myresultt = mycursor.fetchone()
                    for x in myresultt:
                        if fastcash_amount <= x:
                            print("\n\nTransaction Successfully Initiated")
                            mycursor.execute(
                                '''update atm_machine_db set balance = balance - %s WHERE uid=%s''', [(fastcash_amount), (uid)])
                            sb_db.commit()
                        elif fastcash_amount > x:
                            print("\n\nInsufficient Balance")

            elif main_page_input == 2:
                print("\n\n1 - Current \n2 - Savings\n\n")
                cash_method = input("Enter the Method: ")
                withdrawl_amount = int(input("Enter the Amount: "))
                mycursor.execute(
                    '''select balance FROM atm_machine_db WHERE uid=%s''', [(uid)])
                myresultt = mycursor.fetchone()
                for x in myresultt:
                    if withdrawl_amount <= x:
                        print("\n\nTransaction Successfully Initiated")
                        mycursor.execute(
                            '''update atm_machine_db set balance = balance - %s WHERE uid=%s''', [(withdrawl_amount), (uid)])
                        sb_db.commit()
                    elif withdrawl_amount > x:
                        print("\n\nInsufficient Balance")
            elif main_page_input == 3:
                print("1 - Current \n2 - Savings")
                balance_enquiry = int(input("Choose: "))
                if balance_enquiry == 1:
                    mycursor.execute(
                        "SELECT balance FROM atm_machine_db WHERE uid=%s", [(uid)])
                    myresult = mycursor.fetchone()
                    for x in myresult:
                        print("\n\nYour Balance was", x)

            elif main_page_input == 4:
                print("\n\n1 - Last 10 Transaction\n\n")
                obj1.mini_statement()

            elif main_page_input == 5:
                print("\n\n1-Change Pin \n2-Forgot Pin\n\n")
                change_pin = int(input("Choose: "))
                if change_pin == 1:
                    old_pass = input("\n\nEnter Old Pin:")
                    obj1.type("\n\nPlease wait Checking......\n\n")
                    mycursor.execute(
                        "SELECT password FROM atm_machine_db WHERE uid=%s", [(uid)])
                    myresult = mycursor.fetchone()
                    for x in myresult:
                        if old_pass == x:
                            new_pin = int(input("Enter New Pin: "))
                            mycursor.execute(
                                '''update atm_machine_db set password = %s WHERE uid=%s''', [(new_pin), (uid)])
                            sb_db.commit()
                            print("\n\nPin Changed Successfully")
                        else:
                            print("\n\nIncorrect Pin")
                elif change_pin == 2:
                    print("\n\nSorry you need to Go to Bank")

    def login(self, uid, pin):
        sql = "select * from atm_machine_db where uid = %s and password = %s"
        mycursor.execute(sql, [(uid), (pin)])
        results = mycursor.fetchall()
        if results:
            for i in results:
                print("Login Success\n\n")
                obj1.languages()
                break
        else:
            print("\n\nUser Does Not Exist")

    def languages(self):
        print("Choose the Language")
        print('''\n\n1-English \n2-Tamil \n3-Malayalam\n\n''')
        languagess = int(input("Select the Language: "))
        if languagess == 1:
            obj1.main_page()
        elif languagess == 2 or languagess == 3:
            print("Sorry Currently Not Available")

    def mini_statement(n):
        for i in range(0, 10):
            n = random.randint(1000, 15000)
            inicio = datetime(2022, 8, 1)
            final = datetime(2022, 8, 30)
            random_date = inicio + \
                timedelta(seconds=int(
                    (final - inicio).total_seconds() * random.random()))
            print(random_date, "------- Rs.", n)

    def type(self, text):
        words = text
        for char in words:
            time.sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()


print('''
1 - Login
2 - Create a Account''')
obj1 = Atmachine()
get_met = int(input("Enter Method: "))
if get_met == 1 or get_met == 2:
    if get_met == 1:
        uid = int(input("Enter Your Four digit User ID: "))
        pin = int(input("Enter Your Four digit PIN: "))
        obj1.type("Please Wait Validating....\n")
        obj1.login(uid, pin)
    elif get_met == 2:
        uid = int(input("Enter your User ID: "))
        password = int(input("Choose your PIN Number: "))
        FirstName = input("Enter your FirstName: ")
        LastName = input("Enter your LasttName: ")
        mobileno = input("Enter your Mobile No: ")
        Deposit = int(input("Deposit Min Balance (Rs/- 2000): "))
        obj1.register(
            uid, password, FirstName, LastName, mobileno, Deposit)
