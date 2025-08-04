import time

while True:
username = input("what would you like your username to be?")
time.sleep(3)
print("processing...")
time.sleep(3)
confirm = input(f"to confirm, you want your username to be '{username}' correct? (yes/no): ")
if confirm.lower() == "yes":
 password = input("what would you like your password to be?")
  print("Account succesfully created!")
break

else:
  print("okay, lets try again\n")
