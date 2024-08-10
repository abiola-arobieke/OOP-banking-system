class Atm:
    def __init__(self, location, manage_by, balance=0):
        self.location = location
        self.manage_by = manage_by
        self.balance = balance
        self.banks = []
        self.__deposits = []
        self.transaction = []

    @property
    def bank(self):
        """Bank getters method"""
        return self.banks

    @bank.setter
    def bank(self, bank):
        self.banks = bank
        if not self in self.banks.atm:
            bank.atm.append(self)

    def deposit(self, amount):
        """Method for depositing funds in the ATM"""
        if amount < 0:
            raise ValueError('Depositing funds cannot be less than 0')
        self.__deposits.append(amount)
        self.balance += amount

    def get_deposit(self):
        """Method for getting all depsoit"""
        return self.__deposits
    
    def get_transactions(self):
        return self.transaction

    def withdraw(self):
        pass
