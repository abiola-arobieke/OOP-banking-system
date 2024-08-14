"""Module for managing bank class."""

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
        self.__customer = []

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
        """Function for debit card getters"""

        return self.debit_cards

    @debit_card.setter
    def debit_card(self, card):
        self.debit_cards = card

    @property
    def customer(self):
        """Method for customers getter."""

        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    def create_account(self, customer, account, debit_card):
        """Method for creating an account for a customer"""

        self.account.append(account)
        self.customer.append(customer)
        self.debit_card.append(debit_card)

        debit_card.bank = self

        account.bank = self
        account.debit_card = debit_card

        customer.bank.append(self)
        customer.account = account
        customer.debit_card = debit_card

    def add_atm(self, location):
        """Method for adding an ATM to the bank"""

        atm = Atm(location, self)
        self.atms.append(atm)
        atm.bank = self

    def approve_loan(self, acct_num):
        """Method for approving loan request"""

        for account in self.account:
            if account.number == acct_num:
                for loan in self.loans:
                    if loan.account == account and loan.status == "pending":
                        ledger_balance = account.balance - loan.amount
                        loan.credit += loan.amount
                        loan.debt += loan.amount
                        loan.book_balance = ledger_balance
                        account.balance += loan.amount
                        account.book_balance -= loan.amount
                        loan.status = "approved"
                        break
                    else:
                        print("Loan request not found or nor pending")
            else:
                print("No loan request")

    def reject_loan(self, acct_num):
        """Method for rejecting loan request"""

        for account in self.account:
            if account.number == acct_num:
                for loan in self.loans:
                    if loan.account == account and loan.status == "pending":
                        loan.status = "rejected"

    def loan_request(self):
        """Function for getting all loan request"""

        return self.loans

    def find_account(self, acc):
        """Function for searching for an account"""

        for account in self.account:
            if acc == account:
                return account
            return "No match found"

    def get_accounts(self):
        """Method for approving loan request"""

        return self.__account
