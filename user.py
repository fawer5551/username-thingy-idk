import time

while True:
    username = input("What would you like your username to be? ")
    time.sleep(3)
    print("processing...")
    time.sleep(3)
    print("processing..")
    time.sleep(3)
    print("processing.")
    time.sleep(3)

    confirm = input(f"To confirm, you want your username to be '{username}' correct? (yes/no): ")

    if confirm.lower() == "yes":
        password = input("What would you like your password to be? ")
        passconf = input("Enter password again: ")

        if passconf == password:
            print("Password confirmed, please wait...")
            time.sleep(3)
            print("Account successfully created!")
            break
        else:
            print("Passwords do not match. Account has not been created.")
            break
    else:
        print("Okay, let's try again.\n")

