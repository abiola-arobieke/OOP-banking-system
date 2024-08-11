from loan import Loan


class Customer:
    """A class representing a customer"""

    def __init__(self, name, address, password=None, card_number=None, pin=None):
        self.name = name
        self.address = address
        self.password = password
        self.card_number = card_number
        self.pin = pin
        self.accounts = []

    @property
    def account(self):
        return self.accounts

    @account.setter
    def account(self, account):
        self.accounts = account

    def add_account(self, account):
        self.accounts.append(account)
        account.customer = self

    def request_loan(self, amount, acct_number):
        if amount <= 0 or amount > 50000:
            raise ValueError('Invalid amount')

        for account in self.account:
            if account.number == acct_number:
                Loan(amount, account, account.bank)

    def verify_password(self):
        pass
