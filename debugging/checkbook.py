#!/usr/bin/python3
"""
Checkbook Application

A simple terminal-based program to track deposits, withdrawals, and current balance.
"""

class Checkbook:
    """
    A class to represent a simple checkbook with deposit, withdrawal, and balance functionalities.
    """
    def __init__(self):
        """Initializes the checkbook with a starting balance of $0.00."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a positive amount into the checkbook balance.

        Args:
            amount (float): The amount to deposit.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a positive amount from the checkbook balance if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Prints the current balance in the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop of the checkbook program, handles user interaction.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Thank you for using the checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
