"""Module providing a managing the atm activities."""

from loan import Loan


class Customer:
    """A class representing a customer"""

    def __init__(self, name, address, password=None):
        self.name = name
        self.address = address
        self.password = password
        self.card_number = None
        self.pin = None
        self.accounts = []
        self.debit_cards = []
        self.__bank = []

    # def bank(self):
    #     # return self.banks

    @property
    def debit_card(self):
        return self.debit_cards

    @debit_card.setter
    def debit_card(self, debit_card):
        # self.debit_cards = debit_card
        self.debit_cards.append(debit_card)
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
        if amount <= 0 or amount > 50000:
            raise ValueError('Invalid amount')

        for account in self.account:
            if account.number == acct_number:
                Loan(amount, account, account.bank)

    def verify_password(self):
        pass
