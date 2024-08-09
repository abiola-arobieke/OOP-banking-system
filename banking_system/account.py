class Account:
    """Class representing a bank account"""

    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance
        self.banks = []

    @property
    def bank(self):
        return self.banks

    @bank.setter
    def bank(self, bank):
        self.banks = bank
        if not self in self.banks.account:
            self.banks.append(self)

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
