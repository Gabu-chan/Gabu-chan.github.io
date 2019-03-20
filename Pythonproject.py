##turn into multiple accounts
##MAKE SURE TO DO "Must be able to transfer to other user’s account"

import replit
import time

replit.clear()

global action
global accountnumber
global moneyacc1
global moneyacc2
global moneyacc3
global currentaccountmoneytemp

currentaccountmoneytemp = 0
moneyacc1 = 0
moneyacc2 = 0
moneyacc3 = 0

def help():
  print("Press 'b' to display balance.")
  print("Press 'd' to deposit money.")
  print("Press 'w' to withdrawal from your account.")
  print("Press 't' to transfer to an account")
  print("Type 'help' to display these commands again.")
  print("Type 'exit' to leave this ATM.")
  print("When in withdrawal or deposit, type 0 to do nothing.")

def start():
  print("Welcome account number : ", accountnumber)
  help()

def balance():
  print("You currently have", "$", currentaccountmoneytemp)

def deposit():
  global currentaccountmoneytemp
  global d
  d = 0
  try:
    d = float(input("How much would you like to deposit? : "))
  except:
    print("Unknown value entered, returning to menu.")
  if type(d) == float:
    if d < 0:
      print(d, "is a negative, if you want to withdrawal, you should exit and go to withdrawal.")
    else:
      currentaccountmoneytemp = currentaccountmoneytemp + d
      print("Current balance :", currentaccountmoneytemp)

def t():
  global currentaccountmoneytemp
  global moneyacc1
  global moneyacc2
  global moneyacc3
  global accounttransferto
  accounttransferto = "placeholder"
  t = 0


  while accounttransferto == "placeholder":
    accounttransferto = str(input("What account would you like to transfer to? : "))
    if accounttransferto == "41693":
      print("Finding account : ", accounttransferto)
    elif accounttransferto == "38294":
      print("Finding account : ", accounttransferto)
    elif accounttransferto == "48732":
      print("Finding account : ", accounttransferto)
    else:
      print("Finding account : ", accounttransferto)
      print("Invalid account, please try again")
      accounttransferto = "placeholder"
  try:
    t = float(input("How much would you like to transfer? : "))
  except:
    print("Unknown value entered, returning to menu.")
    accounttransferto = "placeholder"
  if type(t) == float:
    if t > currentaccountmoneytemp:
      print(t, "exceeds your current balance of", currentaccountmoneytemp)
      print("Returning to menu.")
      accounttransferto = "placeholder"
    else:
      if accountnumber == accounttransferto:
        print("You can not transfer to your own account.")
        accounttransferto = "placeholder"
      else:
        if accounttransferto == "41693":
          moneyacc1 = moneyacc1 + t
        elif accounttransferto == "38294":
          moneyacc2 = moneyacc2 + t
        elif accounttransferto == "48732":
          moneyacc3 = moneyacc3 + t
        currentaccountmoneytemp = currentaccountmoneytemp - t
        print("Current balance :", currentaccountmoneytemp)
        print("Transfered", t, "to account", accounttransferto)
  accounttransferto = "placeholder"

def withdrawal():
  global currentaccountmoneytemp
  global w
  w = 0
  try:
    w = float(input("How much would you like to withdraw? : "))
  except:
    print("Unknown value entered, returning to menu.")
  if type(w) == float:
    if w > currentaccountmoneytemp:
      print(w, "exceeds your current balance of", currentaccountmoneytemp)
      withdrawal()
    else:
      currentaccountmoneytemp = currentaccountmoneytemp - w
      print("Current balance :", currentaccountmoneytemp)

while 0 == 0:
  global action
  global accountnumber


  accountnumber = -17
  action = "N/A"
  currentaccountmoneytemp = 0


  print("account numbers are '41693' '38294' '48732'")


  while accountnumber == -17:
    accountnumber = input("Input account number : ")
    if accountnumber == "41693":
      print("Accessing account : ", accountnumber)
    elif accountnumber == "38294":
      print("Accessing account : ", accountnumber)
    elif accountnumber == "48732":
      print("Accessing account : ", accountnumber)
    else:
      print("Accessing account : ", accountnumber)
      print("Invalid account, please try again")
      accountnumber = -17
  if accountnumber == "41693":
    currentaccountmoneytemp = moneyacc1
  elif accountnumber == "38294":
    currentaccountmoneytemp = moneyacc2
  elif accountnumber == "48732":
    currentaccountmoneytemp = moneyacc3
  

  start()


  while action != "exit":
    action = input("What do you want to do? : ")
    if action == "b":
      try:
        balance()
      except:
        print("An error occurred, restarting atm to prevent money storage issues...")
        action = "exit"
    elif action == "w":
      try:
        withdrawal()
      except:
        print("An error occurred, restarting atm to prevent money storage issues...")
        action = "exit"
    elif action == "d":
      try:
        deposit()
      except:
        print("An error occurred, restarting atm to prevent money storage issues...")
        action = "exit"
    elif action == "t":
      #try:
      t()
      #except:
        #print("An error occurred, restarting atm to prevent money storage issues...")
        #action = "exit"
    elif action == "help":
      help()
    elif action == "exit":
      print("Exiting . . .")
    else:
      print("Unknown option chosen, try again.")
  print("Thank you for using COMPANY_NAME_ATM. Goodbye. Restarting in 5 seconds...")


  if accountnumber == "41693":
    moneyacc1 = currentaccountmoneytemp
  elif accountnumber == "38294":
    moneyacc2 = currentaccountmoneytemp
  elif accountnumber == "48732":
    moneyacc3 = currentaccountmoneytemp





  time.sleep(5)
  replit.clear()