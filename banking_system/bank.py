from account import Saving, Current


class Bank:
    def __init__(self, code, address):
        self.code = code
        self.address = address
        self.accounts = []

    @property
    def account(self):
        return self.accounts

    @account.setter
    def account(self, account):
        self.account = account

    def add_account(self, account):
        self.accounts.append(account)
        account.banks = self

    def getAccounts(self):
        pass

    def maintain(self):
        pass

    def manages(self):
        pass
