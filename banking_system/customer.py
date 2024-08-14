"""Module providing a managing the atm activities."""

from loan import Loan


class PasswordError(Exception):
    """A class representing a pass exception"""


class Customer:
    """A class representing a customer"""

    def __init__(self, name, address, password='0000'):
        self.name = name
        self.address = address
        self.__password = password
        self.card_number = None
        self.pin = None
        self.accounts = []
        self.__debit_card = []
        self.__bank = []

    @property
    def debit_card(self):
        """Debit card getter method"""
        return self.__debit_card

    @debit_card.setter
    def debit_card(self, debit_card):
        self.__debit_card.append(debit_card)
        debit_card.customer = self

    @property
    def account(self):
        """Account getters method"""
        return self.accounts

    @account.setter
    def account(self, account):
        self.accounts.append(account)
        account.customer = self

    @property
    def bank(self):
        """A getter method for adding a bank"""
        return self.__bank

    def request_loan(self, amount, acct_number):
        """Function for making a loan request"""

        if amount <= 0 or amount > 50000:
            raise ValueError('Invalid amount')

        for account in self.account:
            if account.number == acct_number:
                Loan(amount, account, account.bank)

    def verify_password(self, password):
        """Function for verifying password"""

        if password != self.__password:
            raise PasswordError('Invalid Password')
        return "Password matched"
