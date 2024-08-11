class Loan:
    def __init__(self, amount, account, bank):
        self.amount = amount
        self.status = "pending"  # "pending", "approved", "rejected"
        self.debt = 0
        self.credit = 0
        self.interest = 0
        self.book_balance = account.balance

        self.account = account
        account.loans.append(self)

        self.bank = bank
        bank.loans.append(self)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if amount < 0:
            # Add appropriate error message
            raise ValueError("Loan amount must be positive")
        self.__amount = amount

    def calculate_interest(self, amount):
        pass

    def approve_loan(self, amount):
        pass
