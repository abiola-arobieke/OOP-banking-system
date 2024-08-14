"""Module for managing the atm activities."""


class Atm:
    """Class representing a atm class"""

    def __init__(self, location, manage_by, balance=0):
        self.location = location
        self.manage_by = manage_by
        self.balance = balance
        self.banks = []
        self.__deposits = []
        self.transaction = []

    @property
    def bank(self):
        """Bank getters method"""
        return self.banks

    @bank.setter
    def bank(self, bank):
        self.banks = bank
        if not self in self.banks.atm:
            bank.atm.append(self)

    def deposit(self, amount):
        """Method for depositing funds in the ATM"""

        if amount <= 0:
            raise ValueError('You cannot funds cannot be less than 0')
        self.__deposits.append(amount)
        self.balance += amount

    def withdraw(self, amount):
        """A method for withrawing funds from the atm"""

        if amount > self.balance:
            raise ValueError('You cannot withdraw above the atm balance')
        elif amount <= 0:
            raise ValueError('You cannot withdraw zero or negative amount')
        self.balance -= amount

    def get_all_deposit(self):
        """Method for getting all depsoit"""

        return self.__deposits

    def get_transactions(self):
        """Get all transaction from the atm"""

        return self.transaction

    def check_balance(self):
        """Method for checking the ATM balance"""

        total = 0
        for transaction in self.transaction:
            total += transaction.amount
        return self.deposit - total
