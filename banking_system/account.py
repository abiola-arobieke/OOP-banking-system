class Account:
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance
    
    def deposit(self):
        pass

    def withdraw(self):
        pass


class Saving(Account):
    def __init__(self, number, balance=0):
        super().__init__(number, balance)


class Current(Account):
    def __init__(self, number, balance=0):
        super().__init__(number, balance)
