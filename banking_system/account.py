from transaction import WithdrawTransaction, TransferTransaction


class Account:
    """Class representing a bank account"""

    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance
        self.banks = []
        self.customers = []
        self.transaction = []

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
        self.balance += amount

    def withdraw(self, amount, atm):
        cash = WithdrawTransaction(amount, self, atm)
        cash.withdraw(amount, self, atm)

    def transfer(self, amount, to_account, atm):
        transfer = TransferTransaction(amount, self, to_account, atm)
        transfer.transfer(amount, self, to_account)


class Saving(Account):
    """Class representing a saving account"""

    def __init__(self, number, balance=0):
        self.type = 'Saving'
        super().__init__(number, balance)


class Current(Account):
    """Class representing a current account"""

    def __init__(self, number, balance=0):
        self.type = 'Current'
        super().__init__(number, balance)
