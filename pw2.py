# Usage: type (pw2 <account with saved password>) in windows+R dialog.
import re
import sys
import pyperclip as ppc

# create a regex of the account 
account = sys.argv[1]
account_pattern = re.compile(account+r":(\w+)")






# open a file with passwords
file = open(r"text.txt", "r+")
accounts = file.readlines()
# find a needed account
def finding_account(account):
    try:
        password = account_pattern.search(account)
        password = password.group(1)
        return password
    except AttributeError:
        pass


for i in accounts:
    password = finding_account(i)
    if password!=None:
        break
   
# copy the password of that acccount
if password!= None:
   ppc.copy(password) 
   print("Password for "+ account+" coppied to clippboard")
else:
    print("there is no account named thatway, means nothing to coppy. Sorry)")
    print("Check whether the spelling is correct")
    print("Or if you want to add a new account press Y")
    answer= input().lower()
    if answer == "y":
        password = input("enter a password of "+ account+" ")
        file.write(account+":"+password+"\n")
        print("new account succesfully added")
    elif answer!="y":
        print("bye")
    

        
