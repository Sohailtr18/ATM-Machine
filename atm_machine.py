import time
import random
from datetime import datetime, timedelta
from pyfiglet import Figlet

title_bank = Figlet(font="standard")
print(title_bank.renderText("WELCOME TO DARK-PIRATE BANK"))

time.sleep(1)


class Atmachine():
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def languages(self):
        print("Choose the Language")
        print('''1-English \n2-Tamil \n3-Malayalam''')

    def atm_pin(self, pin):
        self.pin = pin

    def main_page(self):
        print('''1-Fast Cash \n2-Withdrawl \n3-Balance Enquiry \n4-Mini Statement \n5-Pin Change''')

    def fast_cash(self, amount):
        self.amount = amount

    def withdrawl(self, amount):
        self.amount = amount

    def mini_statement(n):
        for i in range(0, 10):
            n = random.randint(1000, 15000)
            inicio = datetime(2022, 8, 1)
            final = datetime(2022, 8, 30)
            random_date = inicio + \
                timedelta(seconds=int(
                    (final - inicio).total_seconds() * random.random()))
            print(random_date, "------- Rs.", n)

    def pin_change(self, change_pin, old_pin, new_pin):
        if change_pin == 1:
            old_pin = old_pin
            if old_pin == old_pin:
                new_pin = new_pin
                print(f"Your New Pin is {new_pin}")
        else:
            print("Incorrect Old Pin")


user_name = input("Enter the USERNAME: ")
password = input("Enter the Password: ")

obj1 = Atmachine(user_name, password)


if user_name == "Sohail" and password == "123":
    obj1.languages()
    languagess = int(input("Select the Language: "))

    if languagess == 1:
        pinn = int(input("Please Enter The Four Digit Pin: "))
        obj1.atm_pin(pinn)

        if pinn == 2525:
            obj1.main_page()
            main_page_input = int(input("Choose the Number: "))

            if main_page_input == 1 or main_page_input == 2 or main_page_input == 3 or main_page_input == 4 or main_page_input == 5:
                if main_page_input == 1:
                    print("Fast Withdrwal Amount Limit 10,000")
                    fastcash_amount = input("Enter the Amount: ")
                    obj1.fast_cash(fastcash_amount)
                    print("Transaction Successfully Initiated")

                elif main_page_input == 2:
                    print("1 - Current \n2 - Savings")
                    cash_method = input("Enter the Method: ")
                    withdrawl_amount = input("Enter the Amount: ")
                    obj1.withdrawl(withdrawl_amount)
                    print("Transaction Successfully Initiated")

                elif main_page_input == 3:
                    print("1 - Current \n2 - Savings")
                    balance_enquiry = int(input("Choose: "))
                    if balance_enquiry == 1:
                        print("25568")

                elif main_page_input == 4:
                    print("1 - Last 10 Transaction")
                    obj1.mini_statement()

                elif main_page_input == 5:
                    print("1-Change Pin \n2-Forgot Pin")
                    change_pin = int(input("Choose: "))
                    if change_pin == 1:
                        oldpin = int(input("Enter Old Pin:"))
                        if oldpin == pinn:
                            new_pin = int(input("Enter New Pin: "))
                            obj1.pin_change(change_pin, oldpin, new_pin)
                            print("Pin Changed Successfully")

        else:
            print("Incorrect Pin")
    elif languagess == 2 or languagess == 3:
        print("Sorry Currently Not Available")
else:
    print("Incorrect Pin")


# fast cash, withdrawl, balance enquiry, Mini statement, Pin change
