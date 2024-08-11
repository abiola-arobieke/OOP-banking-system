from datetime import datetime


class Transaction:
    """A class representing an ATM transaction"""

    def __init__(self, amount, account, atm):
        self.amount = amount
        self.date = datetime.today().strftime('%Y-%m-%d')

        self.account = account
        account.transaction.append(self)

        self.atm = atm
        atm.transaction.append(self)


class WithdrawTransaction(Transaction):
    """A class representing widthraw in ATM"""

    def __init__(self, amount, account, atm):
        self.type = 'withdraw'
        super().__init__(amount, account, atm)

    def withdraw(self, amount, account, atm):
        if atm.balance >= amount:
            if account.balance >= amount:
                account.balance -= amount
                account.book_balance -= amount
                atm.balance -= amount
            else:
                print("Insufficient funds to withdraw")
        else:
            print("Insufficient funds in ATM")


class TransferTransaction(Transaction):
    """A class representing transfer made in an ATM"""

    def __init__(self, amount, account, to_account, atm):
        self.type = 'transfer'
        super().__init__(amount, account, atm)

        self.to_account = to_account

    def transfer(self, amount, account, to_account):
        if account.balance >= amount:
            account.balance -= amount
            account.book_balance -= amount
            to_account.balance += amount
            to_account.book_balance += amount
        else:
            print("Insufficient funds to transfer")
