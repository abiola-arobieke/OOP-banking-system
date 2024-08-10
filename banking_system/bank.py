from account import Saving, Current, Account


class Bank:
    """Class representing a saving account"""

    def __init__(self, code, address):
        self.code = code
        self.address = address
        self.account = []

    @property
    def account(self):
        """Bank account getters"""
        return self.__account

    @account.setter
    def account(self, account):
        self.__account = account

    def add_account(self, account):
        """Function to add new account."""
        self.__account.append(account)
        account.bank = self

    def getAccounts(self):
        pass

    def maintain(self):
        pass

    def manages(self):
        pass
