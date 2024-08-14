"""A file for managing loan"""


class Loan:
    """A class for managing loan"""

    def __init__(self, amount, account, bank):
        self.amount = amount
        self.status = "pending"
        self.debt = 0
        self.credit = 0
        self.interest = amount
        self.book_balance = account.balance

        self.account = account
        account.loans.append(self)

        self.bank = bank
        bank.loans.append(self)

    @property
    def interest(self):
        """A getter method getting interest"""
        return self.__interest

    @interest.setter
    def interest(self, amount):
        self.__interest = amount * 0.09 * 2

    @property
    def amount(self):
        """A getter method getting amount"""

        return self.__amount

    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise ValueError("Amount must be greater than zero")
        self.__amount = amount

    def calculate_interest(self, amount, time):
        """Function for calculating interest"""
        rate = 0.09
        interest = amount * rate * time
        return interest
