import mysql.connector as aql
import sys, hashlib, random

mycon = aql.connect(host="localhost", user="root", passwd="mypasssql", database="bank")
if mycon.is_connected():
    print("Sucessfully connected to MySQL database.")
    cursor = mycon.cursor()


class customer():
    pass


def signup(email, pwd):
    while True:
        conf_pwd = input("Confirm your Password:")
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            f = open(f"credentail{account_name}.txt", "a")
            f.write(email + "\n")
            f.write(hash1)
            f.close()
            print("You Have Registered Successfully!")
            global ps
            ps = str(random.randint(1000, 9999))
            passave()
            name = customer()
            name.pin = ps
            print("Your PIN is", name.pin)
            print("Please Note the PIN")
            break
        else:
            print("Password is not same as above! Try Again\n")
            pass


def login():
    global name, ff
    name = input("Enter Your name:")
    ff = str(name)
    email = input("Enter Email:")
    pwd = input("Enter Password:")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open(f"credentail{ff}.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
        print("Logged in Successfully!")
        global g
        g = True
    else:
        print("Enter Valid Username or Password! \n")


def passave():
    enc = ps.encode()
    hash1 = hashlib.md5(enc).hexdigest()

    f = open(f"paswd{account_name}.txt", "w")
    f.write(hash1)
    f.close()


def paschk():
    auth = ps.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open(f"paswd{name}.txt", "r") as f:
        stored_pin = f.read()
    f.close()
    if auth_hash == stored_pin:
        print("Verified")
        global acc
        acc = True
    else:
        "Incorrect PIN"


def details():
    account_no = int(input("Enter account number: "))
    print()
    cursor.execute("select * from customer_details where account_no=" + str(account_no))
    if cursor.fetchone() is None:
        print()
        print("Invalid account number.")
    else:
        data = cursor.fetchall()
        for row in data:
            print("Password:", row[0])
            print()
            print("Account name", row[1])
            print()
            print("Account number", row[2])
            print()
            print("Phone number: ", row[3])
            print()
            print("Address", row[4])
            print()
            print("Current amount in your account", row[5])
            print()


def more_details():
    ask = input("Do you want to see someone else's details?...(y/n)")
    if ask == "y":
        details()
    else:
        print()


def update():
    account_no = int(input("Enter account number: "))
    cursor.execute("select * from customer_details where account_no=" + str(account_no))
    cursor.fetchall()
    count = cursor.rowcount
    mycon.commit()
    if count == 0:
        print()
        print("Account number invalid. Sorry try again later.")
        print()
    else:
        print()
        print("What do you want to update?")
        print("1. Password")
        print("2. Account holder's name")
        print("3. Account holder's phone number")
        print("4. Account holder's address")
        print()
        x = int(input("Enter your choice: "))
        if x == 1:
            new_password = int(input("Enter the new password:"))
            cursor.execute(
                "update customer_details set password=" + str(new_password) + " where account_no=" + str(account_no))
            mycon.commit()
            print()
            print("Account updated succesfully.")
        elif x == 2:
            new_name = input("Enter the new name:")
            cursor.execute(f'update customer_details set account_name="{new_name}" where account_no=' + str(account_no))
            mycon.commit()
            print()
            print("Account updated succesfully.")
        elif x == 3:
            new_ph_number = int(input("Enter the new phone number: "))
            cursor.execute(f"update customer_details set ph_number={new_ph_number} where account_no=" + str(account_no))
            mycon.commit()
            print()
            print("Account updated succesfully.")
        elif x == 4:
            new_address = input("Enter the new address: ")
            cursor.execute(f'update customer_details set address="{new_address}" where account_no=' + str(account_no))
            mycon.commit()
            print()
            print("Account updated succesfully.")


def again():
    ask = input("Do you want to update something else also?... (y/n)")
    if ask == "y":
        update()
    else:
        print()


print("======== WELCOME TO NEWDAY BANK =========")
print("1. CREATE BANK ACCOUNT")
print()
print("2. TRANSACTION")
print()
print("3. DISPLAY CUSTOMER DETAILS")
print()
print("4. DELETE ACCOUNT")
print()
print("5. UPDATE CUSTOMER DETAILS")
print()
print("6. QUIT")
print()
n = int(input("Enter your choice: "))
print()
if n == 1:
    password = input("Enter new account password:")
    print()
    account_name = input("Enter account holder's name:")
    print()
    account_no = int(input("Enter account number:"))
    print()
    ph_number = int(input("Enter phone number:"))
    print()
    acc_email = input("Enter Your Email Address")
    print()
    address = input("Enter current address:")
    print()
    print("The minimum amount that should be in the account is Rs.1000.")
    print()
    signup(acc_email, password)
    cr_amount = int(input("Enter amount you want to add in the account: "))
    cursor.execute(
        f'insert into customer_details values ("{password}","{account_name}",{account_no},{ph_number},"{address}",{cr_amount})')
    mycon.commit()
    print()
    print("Account created successfully.")
elif n == 2:
    while True:
        login()
        if g == True:
            break
    account_no = int(input("Enter Your Account Number:"))
    cursor.execute("select * from customer_details where account_no=" + str(account_no))
    data = cursor.fetchall()
    count = cursor.rowcount
    mycon.commit()
    if count == 0:
        print()
        print("Account number invalid. Sorry try again later.")
        print()
    else:
        print()
        print("1. Withdraw amount")
        print()
        print("2. Add amount")
        print()
        x = int(input("Enter your choice: "))
        print()
        if x == 1:
            paschk()
            amount = int(input("Enter the amount to be withdrawn : "))
            cursor.execute(
                "update customer_details set cr_amount=cr_amount -" + str(amount) + " where account_no=" + str(
                    account_no))
            mycon.commit()
            print()
            print("Account updated succesfully.")
        if x == 2:
            paschk()
            amount = int(input("Enter the amount to be added: "))
            cr_amount = 0
            cursor.execute(
                "update customer_details set cr_amount=cr_amount+" + str(amount) + " where account_no=" + str(
                    account_no))
            mycon.commit()
            print()
            print("Account updated succesfully.")
elif n == 3:
    while True:
        login()
        if g == True:
            break
    details()
    more_details()
elif n == 4:
    while True:
        login()
        if g == True:
            break
    print("Delete accout")
    account_no = int(input("Enter account number :"))
    while count <= 3:
        if acc == False:
            pas = str(input("Enter Your PIN:"))
            paschk()
        elif acc == True:
            cursor.execute("delete from customer_details where account_no=" + str(account_no))
            mycon.commit()
            print("Account deleted successfully")
        count += 1
        print("Invalid PIN")
        print("Attempts Left", 4 - count)
    else:
        print("You Have Reached Maximum Attempt Limit")
        print("Your Account has Been Frezzed")
        sys.exit()
elif n == 5:
    while True:
        login()
        if g == True:
            break
    while count <= 3:
        if acc == False:
            pas = str(input("Enter Your PIN:"))
            paschk()
        elif acc == True:
            update()
            again()
        count += 1
        print("Invalid PIN")
        print("Attempts Left", 4 - count)
    else:
        print("You Have Reached Maximum Attempt Limit")
        print("Your Account has Been Frezzed")
        sys.exit()
elif n == 6:
    print("Do you want to exit?... (y/n)")
    c = input("Enter your choice: ")
    if c == "y":
        print("Closed successfully.")
        sys.exit()
else:
    print("Select a valid option")