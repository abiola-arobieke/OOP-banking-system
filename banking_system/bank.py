from account import Saving, Current


class Bank:
    """Class representing a saving account"""

    def __init__(self, code, address):
        self.code = code
        self.address = address
        self.account = []
        self.atms = []
        self.loans = []

    @property
    def atm(self):
        """ATM getters method"""
        return self.atms

    @atm.setter
    def atm(self, atm):
        self.atms = atm

    @property
    def account(self):
        """Bank account getters"""
        return self.__account

    @account.setter
    def account(self, account):
        self.__account = account

    def create_account(self, customer, number, balance=0, acc_type='saving'):
        """Method for creating an account for a customer"""
        if acc_type == 'saving':
            new_account = Saving(number, balance)
            self.account.append(new_account)
            new_account.bank = self
            customer.add_account(new_account)
        else:
            new_account = Current(number, balance)
            self.account.append(new_account)
            new_account.bank = self
            customer.add_account(new_account)

    def add_atm(self, atm):
        """Method for adding an ATM to the bank"""
        self.atms.append(atm)
        atm.bank = self

    # Deprecated method. Remember to remove
    def add_account(self, account):
        """Function to add new account."""
        self.__account.append(account)
        account.bank = self

    def approve_loan(self, acct_num):
        for account in self.account:
            if account.number == acct_num:
                for loan in self.loans:
                    if loan.account == account and loan.status == "pending":
                        ledger_balance = account.balance - loan.amount
                        loan.credit += loan.amount
                        loan.debt += loan.amount
                        loan.book_balance = ledger_balance
                        account.balance += loan.amount
                        account.book_balance = ledger_balance
                        loan.status = "approved"
                        break
                    else:
                        print("Loan request not found or nor pending")
            else:
                print("No loan request")

    def getAccounts(self):
        pass

    def maintain(self):
        pass

    def manages(self):
        pass
