class Atm:
    def __init__(self, location, manage_by):
        self.location = location
        self.manage_by = manage_by
        self.banks = []

    @property
    def bank(self):
        return self.banks

    @bank.setter
    def bank(self, bank):
        self.banks = bank
        if not self in self.banks.atm:
            bank.atm.append(self)


    def withdraw(self):
        pass

    def deposit(self):
        pass

    def check_balance(self):
        pass
