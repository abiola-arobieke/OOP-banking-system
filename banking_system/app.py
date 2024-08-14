"""Module for managing the banking activities."""

from bank import Bank
from atm import Atm
from customer import Customer
from account import Saving, Current
from debit_card import DebitCard

first_bank = Bank('80078', 'Onikan, Lagos')
gt_bank = Bank('80456', 'Berger, Lagos')

cust1 = Customer('Van Persie', 'Surulere, Lagos')
cust2 = Customer('John Travola', 'Ojodu, Lagos')

acct1 = Saving(23456729803, 2000)
acct2 = Current(2416387892)
acct3 = Saving(4527729803, 5000)

card1 = DebitCard(first_bank)
card2 = DebitCard(first_bank)
card3 = DebitCard(gt_bank)


first_bank.create_account(cust1, acct1, card1)
first_bank.create_account(cust2, acct2, card2)
gt_bank.create_account(cust1, acct3, card3)

atm1 = Atm('Onikan, Lagos', first_bank)
atm1.deposit(50000)
atm2 = Atm('Onikan, Lagos', first_bank)

first_bank.add_atm('Dugbe, Ibadan')
first_bank.add_atm('Challenge, Ibadan')


print(f'First Bank Accounts:  {first_bank.account}')
print(f'First Bank Customers: {first_bank.customer}')
print(f'First Bank Debit Cards: {first_bank.debit_card}')
print('\n')

print(f'GTBank Accounts: {gt_bank.account}')
print(f'GTBank Debit cards: {first_bank.debit_card}')
print('\n')

print(f'Customer1 Banks: {cust1.bank}')
print(f'Customer Account: {cust1.account}')
print(f'Customer Debit Cards: {cust1.debit_card}')
print('\n')

print(f'Account1 Bank: {acct1.bank}')
print(f'Account1 Debit Card: {acct1.debit_card.card_number}')
print(f'Account1 Holder: {acct1.customer.name}')
print('\n')

print(f'Debit card account: {card1.account}')
print(f'Debit card bank: {card1.bank}')
print('\n')

for account in cust1.account:
    if account.number == 23456729803:
        account.withdraw(1000, atm1)
        print(f'Acct bal after withdrawal: {account.balance}')
        print(f'Debit card no: {account.debit_card.card_number}')
        print(f'Debit card ccv: {account.debit_card.ccv}')
