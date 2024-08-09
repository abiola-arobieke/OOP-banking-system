from account import Saving, Current


class Bank:
    def __init__(self, code, address):
        self.code = code
        self.address = address
        self.account = []

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account):
        self.__account = account

    def add_account(self, account):
        self.__account.append(account)
        account.bank = self

    def getAccounts(self):
        pass

    def maintain(self):
        pass

    def manages(self):
        pass
