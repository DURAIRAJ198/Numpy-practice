# ATM Project in Python
# Features: Check balance, Deposit money, Withdraw money, Exit

balance = 1000.0

print("Welcome to the ATM")

while True:
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: Rs.{balance:.2f}")

    elif choice == '2':
        amount = float(input("Enter amount to deposit: Rs."))
        if amount > 0:
            balance += amount
            print(f"Rs.{amount:.2f} deposited successfully.")
            print(f"Updated balance: Rs.{balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive amount.")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: Rs."))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"Rs.{amount:.2f} withdrawn successfully.")
                print(f"Remaining balance: Rs.{balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive amount.")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
