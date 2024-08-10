class Account:
    """Class representing a bank account"""

    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance
        self.banks = []
        self.customers = []

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

    def deposit(self):
        pass

    def withdraw(self):
        pass


class Saving(Account):
    """Class representing a saving account"""

    def __init__(self, number, balance=0):
        super().__init__(number, balance)


class Current(Account):
    """Class representing a current account"""

    def __init__(self, number, balance=0):
        super().__init__(number, balance)
