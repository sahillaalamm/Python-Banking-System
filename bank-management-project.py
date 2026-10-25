import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():

            with open(database) as fs:
                data = json.loads(fs.read())        
        else:
            print("No such files exists")
    
    except Exception as err:
        print(f"An error occured as {err}")


    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        spchr = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spchr
        random.shuffle(id)
        return "".join(id)


    def Createaccount(self):
        info = {
            "name" : input("Tell your Name- "),
            "age" : int(input("Tell your Age- ")),
            "email" : input("Tell your Email- "),
            "pin" : input("Tell your 4 digit Pin- "),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("You cannot create account")

        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Pls note down your account number")

            Bank.data.append(info)

            Bank.__update()


    def depositmoney(self):
        acctnumber = input("Enter your Account Number- ")
        pin = input("Tell you Pin- ")

        userData = [i for i in Bank.data if i ['accountNo.']== acctnumber and i['pin'] == pin]

        if not userData:
            print("Sorry No Data Found")

        else:
            amount = int(input("How much money you want to deposit- "))
            if amount > 10000 or amount < 0:
                print("Sorry the Amount is too much, you can deposit below 10000 and above 0")

            else:
                userData[0]['balance'] += amount
                Bank.__update()
                print("Amount Deposited Successfully")


    def withdrawmoney(self):
        acctnumber = input("Enter your Account Number- ")
        pin = input("Tell you Pin- ")
        
        userData = [i for i in Bank.data if i ['accountNo.']== acctnumber and i['pin'] == pin]
        
        if not userData:
            print("Sorry No Data Found")
        
        else:
            amount = int(input("How much money you want to Withdraw- "))
            if userData[0]['balance'] < amount:
                print("Sorry you don't have enough money")
                        
        
            else:
                userData[0]['balance'] -= amount
                Bank.__update()
                print("Amount Withdrawn Successfully")


    def showdetails(self):
        acctnumber = input("Enter your Account Number- ")
        pin = input("Tell you Pin- ")

        userData = [i for i in Bank.data if i ['accountNo.']== acctnumber and i['pin'] == pin]

        print("Your Information are- \n")

        for i in userData[0]:
            print(f"{i} : {userData[0][i]}")


    def updatedetails(self):
        acctnumber = input("Enter your Account Number- ")
        pin = input("Tell you Pin- ")
        
        userData = [i for i in Bank.data if i ['accountNo.']== acctnumber and i['pin'] == pin]

        if userData == False:
            print("No such user found")

        else:
            print("You cannot change the Age, Account Number, Balance")

            print("Fill the details for change or leave it empty if no change")

            newData = {
                "name" : input("Tell correct name to update or press enter to skip- "),
                "email" : input("Tell your new email or press enter to skip- "),
                "pin" : input("Tell you new pin or press enter to skip- ")
            }

            if newData["name"] == "":
                newData["name"] == userData[0]["name"]

            if newData["email"] == "":
                newData["email"] == userData[0]["email"]

            if newData["pin"] == "":
                newData["pin"] == userData[0]["pin"]

            newData["age"] = userData[0]["age"]
            newData["accountNo."] = userData[0]["accountNo."]
            newData["balance"] = userData[0]["balance"]

            if type(newData["pin"]) == str:
                newData["pin"] = newData["pin"]

            for i in newData:
                if newData[i] == userData[0][i]:
                    continue

                else:
                    userData[0][i] = newData[i]

            Bank.__update()
            print("Details updated successfully")


    def Delete(self):
        acctnumber = input("Enter your Account Number- ")
        pin = input("Tell you Pin- ")
                
        userData = [i for i in Bank.data if i ['accountNo.']== acctnumber and i['pin'] == pin]

        if userData == False:
            print("Sorry no such Data Exists")

        else:
            check = input("Press Y if you actually want to delete the account or press N")

            if check == "N" or check == "n":
                print("Bypassed")

            else:
                index = Bank.data.index(userData)
                print("Account deleted successfully")
                Bank.__update


user = Bank()
print("Press 1 for Creating an Account- ")
print("Press 2 for Depositing Money- ")
print("Press 3 for Withdrawing Money- ")
print("Press 4 for Showing Details- ")
print("Press 5 for Updating Details- ")
print("Press 6 for Deleting Account- \n")

check = int(input("Tell your response- "))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()

