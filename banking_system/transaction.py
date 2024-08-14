"""File for managing the atm transactions"""

from datetime import datetime
from dataclasses import dataclass


@dataclass
class Transaction:
    """A class representing an ATM transaction"""

    def __init__(self, amount: int, account: object, atm: object):
        self.amount = amount
        self.date = datetime.today().strftime('%Y-%m-%d')

        self.account = account
        account.transaction.append(self)

        self.atm = atm
        atm.transaction.append(self)


class WithdrawTransaction(Transaction):
    """A class representing widthraw in ATM"""

    def __init__(self, amount: int, account: object, atm: object):
        self.type = 'withdraw'
        super().__init__(amount, account, atm)

    def withdraw(self, amount, account, atm):
        """A class representing widthraw in ATM"""

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

    def __init__(self, amount: int, account: object, to_account: object, atm: object):
        self.type = 'transfer'
        super().__init__(amount, account, atm)

        self.to_account = to_account

    def transfer(self, amount, account, to_account):
        """Function for transfer funds to another account in the ATM"""

        if account.balance >= amount:
            account.balance -= amount
            account.book_balance -= amount
            to_account.balance += amount
            to_account.book_balance += amount
        else:
            print("Insufficient funds to transfer")
