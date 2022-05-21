print("Welcome to MAIYO Bank!")

pin = 5678
chances = 3
balance = 50000

while chances!= 0:
    user_pin = int(input("Please enter the four digit pin: "))
    if user_pin != pin:
        chances -= 1
        print("Wrong pin number")
        print(f"You have {chances} chances left")
    else:
        user_choice = input("B : balance, D : deposit, W : withdraw")
        if user_choice == "B":
            print(f"Your total balance is Ksh. {balance}")
        if user_choice == "D":
            deposit_user = int(input("Enter the amount that you would like to deposit: "))
            total_balance = deposit_user + balance
            print(f"You have deposited Ksh. {deposit_user}")
            print(f"You total balance is Ksh. {total_balance}")
        if user_choice == "W":
            withdraw_user = int(input("Enter the amount you want to withdraw: "))
            total_balance = balance - withdraw_user
            print(f"You have withdrawn Ksh. {withdraw_user}")
            print(f"You total balance is Ksh. {total_balance}")
        user_exit = input("Would you like to exit? (Yes/No)")
        if user_exit == "Yes":
            print("Thank you for using MAIYO Bank")
            break
        else:
            continue
