# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 100000  # Maximum loan amount
INTEREST_RATE = 0.05  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    name = input("Enter account holder's name: ")
    if name in account_holders:
        print("Account already exists.")
    else:
        # 2. Add the new account holder to the list of account holders.
        account_holders.append(name)
        # 3. Initialize the balance to 0 for the new account.
        balances.append(0.0)  # Initialize balance to 0
        # 4. Initialize an empty transaction history for the new account.
        transaction_histories.append([])  # Empty transaction history
        # 5. Initialize the outstanding loan amount to 0.
        loans.append(0.0)  # No loan initially
        # 6. Notify the user of the successful account creation.
        print(f"Account created for {name}.")


def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    name = input("Enter account holder's name: ")
    # 2. Check if the account exists in the system.
    if name in account_holders:
        index = account_holders.index(name)
        # 3. If the account exists, prompt the user for the amount to deposit.
        amount = float(input("Enter amount to deposit: "))
        # 4. Update the account's balance with the deposited amount.
        balances[index] += amount
        # 5. Log the transaction in the account's transaction history.
        transaction_histories[index].append(f"Deposited {amount:.2f}")
        # 6. Display the updated balance to the user.
        print(f"Deposited {amount:.2f} to {name}'s account. New balance: {balances[index]:.2f}")
    else:
        # 7. If the account does not exist, inform the user.
        print("Account not found.")


def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    name = input("Enter account holder's name: ")
    # 2. Check if the account exists in the system.
    if name in account_holders:
        index = account_holders.index(name)
        # 3. If the account exists, prompt the user for the amount to withdraw.
        amount = float(input("Enter amount to withdraw: "))
        # 4. Check if there are sufficient funds for the withdrawal.
        if balances[index] >= amount:
            # 5. If funds are sufficient, update the balance and log the transaction.
            balances[index] -= amount
            transaction_histories[index].append(f"Withdrew {amount:.2f}")
            # 6. Display the updated balance to the user.
            print(f"Withdrew {amount:.2f} from {name}'s account. New balance: {balances[index]:.2f}")
        # 7. If insufficient funds, inform the user.
        else:
            print("Insufficient funds.")
    else:
        # 8. If the account does not exist, inform the user.
        print("Account not found.")


def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    name = input("Enter account holder's name: ")
    # 2. Check if the account exists in the system.
    if name in account_holders:
        index = account_holders.index(name)
        # 3. If the account exists, display the current balance.
        print(f"{name}'s balance: {balances[index]:.2f} leva")
    else:
        # 4. If the account does not exist, inform the user.
        print("Account not found.")


def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if account_holders:
        # 2. If there are accounts, loop through each account holder.
        for i, name in enumerate(account_holders):
            # 3. Display the account holder's name, balance, and outstanding loan amount.
            print(f"Account holder: {name}, Balance: {balances[i]:.2f}, Loan: {loans[i]:.2f}")
    else:
        # 4. If there are no accounts, inform the user.
        print("No accounts in the system.")


def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    sender = input("Enter sender's account holder name: ")
    recipient = input("Enter recipient's account holder name: ")

    # 2. Check if both accounts exist in the system.
    if sender in account_holders and recipient in account_holders:
        sender_index = account_holders.index(sender)
        recipient_index = account_holders.index(recipient)
        # 3. If both accounts exist, prompt the user for the amount to transfer.
        amount = float(input("Enter amount to transfer: "))

        # 4. Check if the sender has sufficient funds for the transfer.
        if balances[sender_index] >= amount:
            # 5. If funds are sufficient, update both balances and log the transactions.
            balances[sender_index] -= amount
            balances[recipient_index] += amount
            transaction_histories[sender_index].append(f"Transferred {amount:.2f} to {recipient}")
            transaction_histories[recipient_index].append(f"Received {amount:.2f} from {sender}")
            # 6. Inform the user of the successful transfer.
            print(f"Transferred {amount:.2f} from {sender} to {recipient}.")
        else:
            # 7. If insufficient funds or if either account does not exist, inform the user.
            print("Insufficient funds.")
    else:
        # 7. If insufficient funds or if either account does not exist, inform the user.
        print("One or both accounts not found.")


def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    name = input("Enter account holder's name: ")
    # 2. Check if the account exists in the system.
    if name in account_holders:
        index = account_holders.index(name)
        # 3. If the account exists, display the transaction history.
        history = transaction_histories[index]
        if history:
            for transaction in history:
                print(transaction)
        else:
            # 4. If there are no transactions, inform the user.
            print("No transactions found.")
    else:
        # 5. If the account does not exist, inform the user.
        print("Account not found.")


def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")