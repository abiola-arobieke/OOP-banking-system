import random


class DebitCard:
    def __init__(self, card_number, owner_by):
        self.card_number = card_number
        self.owner_by = owner_by
        self.ccv = random.randint(100, 999)
        self.banks = []
        self.atms = []
        self.accounts = None
        self.customers = []

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, cardnumber):
        if not len(str(cardnumber)) == 24:
            raise ValueError("Card number must be 24 digits long")
        self.__card_number = cardnumber

    @property
    def account(self):
        return self.accounts

    @account.setter
    def account(self, acc):
        self.accounts = acc

    def add_account(self, account):
        self.accounts = account
        account.debit_cards = self

    @property
    def bank(self):
        return self.banks

    @bank.setter
    def bank(self, debit_card):
        self.banks = debit_card
        if not self in self.banks.debit_card:
            self.banks.debit_card.append(self)
