"""Module for managing the account activities."""

from transaction import WithdrawTransaction, TransferTransaction
from loan import Loan


class Account:
    """Class representing a bank account"""

    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance
        self.book_balance = balance
        self.banks = []
        self.customers = []
        self.transaction = []
        self.loans = []

    @property
    def bank(self):
        """A getter method for adding a bank"""
        return self.banks

    @bank.setter
    def bank(self, bank):
        self.banks = bank
        if not self in self.banks.account:
            self.bank.append(self)

    @property
    def customer(self):
        """A getter method for adding a customer"""

        return self.customers

    @customer.setter
    def customer(self, customer):
        self.customers = customer
        if not self in self.customers.account:
            customer.account.append(self)

    def deposit(self, amount):
        """A method for depositing funds in the customer account"""

        self.balance += amount
        self.book_balance += amount

    def withdraw(self, amount, atm):
        """A method for withdrawing funds in the customer account at the atm"""

        cash = WithdrawTransaction(amount, self, atm)
        cash.withdraw(amount, self, atm)

    def transfer(self, amount, to_account, atm):
        """A method for transferring funds at the atm"""

        transfer = TransferTransaction(amount, self, to_account, atm)
        transfer.transfer(amount, self, to_account)

    # @classmethod
    def request_loan(self, amount, bank):
        """Function performing a loan request"""


class Saving(Account):
    """Class representing a saving account"""

    def __init__(self, number, balance=0):
        self.type = 'Saving'
        super().__init__(number, balance)

    def request_loan(self, amount, bank):
        if amount <= 0:
            raise ValueError('Invalid request')
        Loan(amount, self, bank)


class Current(Account):
    """Class representing a current account"""

    def __init__(self, number, balance=0):
        self.type = 'Current'
        super().__init__(number, balance)

    def request_loan(self, amount, bank):
        Loan(amount, self, bank)
