import random


class DebitCard:
    def __init__(self, owner_by):
        self.owner_by = owner_by
        self.card_number = random.randint(1000000000000000, 9999999999999999)
        self.ccv = random.randint(100, 999)
        # self.banks = []
        self.atms = []
        self.accounts = []
        self.customer = []
        self.banks = []

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, cardnumber):
        if not len(str(cardnumber)) == 16:
            raise ValueError("Card number must be 16 digits long")
        self.__card_number = cardnumber

    @property
    def bank(self):
        """A getter method for adding a bank"""
        return self.banks

    @bank.setter
    def bank(self, bank):
        self.banks = bank
        if not self in self.banks.debit_card:
            bank.debit_card.append(self)

    @property
    def account(self):
        return self.accounts

    @account.setter
    def account(self, acc):
        self.accounts = acc
