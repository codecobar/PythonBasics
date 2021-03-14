###login system the user have to be able to enter if he or she is new or have already a account , the program have to store and read the values in dictionaries
## usr and password
# datastore = dict()
import ast


def AddItem(username, password, password1):
    dictionary = {}
    if password1 == password:

    else:
        print("You've enter the wrong password try again")


answer1 = input("ENTER REGISTER OR LOGIN")

if answer1.lower() == "register" or answer1.lower() == " register" or answer1.lower() == "register ":
    while True:
        username = input("Enter a new username: ")
        password = int(input("Enter a password: "))
        password1 = int(input("Enter a password: "))
        AddItem(username, password, password1)

elif answer1.lower() == "login" or answer1.lower() == " login" or answer1.lower() == "login ":
    while True:
        username = input("Enter the username: ")
        password = int(input("Enter the password: "))
        file2 = open("data.txt", "r")
        content = file2.read()
        dictionary = ast.literal_eval(content)
        print(dictionary)
        file2.close()
else:
    print("You've to enter either register or login")
