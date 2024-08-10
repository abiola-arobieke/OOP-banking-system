class Transaction:
    """A class representing an ATM transaction"""

    def __init__(self, amount, account, atm):
        self.amount = amount

        self.account = account
        account.transaction.append(self)

        self.atm = atm
        atm.transaction.append(self)


class WithdrawTransaction(Transaction):
    def __init__(self, amount, account, atm):
        self.transaction_type = 'withdraw'
        super().__init__(amount, account, atm)

    def withdraw(self, amount, account, atm):
        if atm.deposit >= amount:
            if account.balance >= amount:
                account.balance -= amount
            else:
                print("Insufficient funds to withdraw")
        else:
            print("Insufficient funds in ATM")


class TransferTransaction(Transaction):
    def __init__(self, amount, account, to_account, atm):
        self.transaction_type = 'transfer'
        super().__init__(amount, account, atm)

        self.to_account = to_account

    def transfer(self, amount, account, to_account):
        if account.balance >= amount:
            account.balance -= amount
            to_account.balance += amount
        else:
            print("Insufficient funds to transfer")
