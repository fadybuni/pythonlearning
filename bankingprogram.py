def show_balance():
    print(f"Your account balance is ${balance}! ")

def deposit():
    global balance
    print()
    depositamnt = int(input("Please enter how much you would like to deposit: "))
    if depositamnt <= 0:
        print("Invalid Amount")
        print()
    else:
        balance += depositamnt
        print(f"You have successfully deposited {depositamnt}!")
        print()
def withdraw():
    global balance
    print()
    withdrawamnt = int(input("Please enter how much you would like to withdraw: "))
    print()
    if withdrawamnt <= 0:
        print("Invalid amount.")
        print()
    elif withdrawamnt > balance:
        print(f"Invalid amount, You currently have ${balance} available to withdraw!")
        print()
    else:
        balance -= withdrawamnt
        print(f"You have successfully withdrawn ${withdrawamnt}! You new account balance is ${balance}.") 
        print()
balance = 0
is_running = True

def main()
    while is_running:
        print("Banking Program")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("-=-=-=-=-=-=-=-=-=-=-=-")

        choice = input("Enter Your Chhoice (1-4): ")
        print("-=-=-=-=-=-=-=-=-=-=-=-")

        if choice == "1":
            show_balance()
        elif choice =="2":
            deposit()
        elif choice =="3":
            withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("That is a invalid choice")
        print("-=-=-=-=-=-=-=-=-=-=-=-")

    print("Thank you, Have a good day!")



