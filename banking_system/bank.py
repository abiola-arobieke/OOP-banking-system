"""Module for managing bank class."""

from account import Saving, Current
from atm import Atm


class Bank:
    """Class representing a saving account"""

    def __init__(self, code, address):
        self.code = code
        self.address = address
        self.account = []
        self.atms = []
        self.loans = []
        self.debit_cards = []
        self.__customers = []

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

    @property
    def debit_card(self):
        return self.debit_cards

    @debit_card.setter
    def debit_card(self, card):
        self.debit_card = card

    @property
    def customer(self):
        return self.__customers

    def add_debit_card(self, debit_card):
        debit_card.bank = self
        self.debit_cards.append(debit_card)

    def create_account(self, customer, number, balance=0, acc_type='saving'):
        """Method for creating an account for a customer"""

        if acc_type == 'saving':
            new_account = Saving(number, balance)
            self.account.append(new_account)
            new_account.bank = self
            customer.add_account(new_account)
            customer.bank.append(self)
            self.customer.append(customer)

        else:
            new_account = Current(number, balance)
            self.account.append(new_account)
            new_account.bank = self
            customer.add_account(new_account)
            customer.bank.append(self)
            self.customer.append(customer)

    def add_atm(self, location):
        """Method for adding an ATM to the bank"""

        atm = Atm(location, self)
        self.atms.append(atm)
        atm.bank = self

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

    def reject_loan(self, acct_num):
        for account in self.account:
            if account.number == acct_num:
                for loan in self.loans:
                    if loan.account == account and loan.status == "pending":
                        loan.status = "rejected"

    def loan_request(self):
        return self.loans

    def find_account(self, acc):
        for account in self.account:
            if acc == account:
                return account
            print("No match found")

    def getAccounts(self):
        pass

    def maintain(self):
        pass

    def manages(self):
        pass
