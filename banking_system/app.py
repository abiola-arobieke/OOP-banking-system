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
acct3 = Saving(4527729803, 2000)

card1 = DebitCard(first_bank)
card2 = DebitCard(first_bank)
card3 = DebitCard(gt_bank)


first_bank.create_account(cust1, acct1, card1)
first_bank.create_account(cust2, acct2, card2)


gt_bank.create_account(cust1, acct3, card3)



print(f'First Bank Accounts:  {first_bank.account}')
print('bank customers', first_bank.customer)
print(gt_bank.account)
# print(card1.account)

print('First Bank debit cards: ' ,first_bank.debit_card)

print('customer banks', cust1.bank)

print('acct bank: ', acct1.bank)
print('acct debit card: ', acct1.debit_card.card_number)
print('acct customer: ', acct1.customer.name)


print('Debit card account: ', card1.account)
print('Debit card bank: ', card1.bank)


print('customer account: ', cust1.account)
print('customer debit cards: ', cust1.debit_card)

# print(gt_bank.account)
# gt_bank.create_account(cust1, 2352789123)
# first_bank.create_account(cust2, 4352789123)


atm1 = Atm('Onikan, Lagos', first_bank)
atm1.deposit(50000)
atm2 = Atm('Onikan, Lagos', first_bank)

first_bank.add_atm('Dugbe, Ibadan')
first_bank.add_atm('Challenge, Ibadan')

for account in cust1.account:
    if account.number == 23456729803:
        account.withdraw(1000, atm1)
        print(account.balance)
        print(account.debit_card.card_number)
        print(account.debit_card.ccv)


# print(first_bank.customer)

# for cust in first_bank.customer:
# for bank in cust1.bank:
#     print(bank.code)
# print(cust.account)
# print(cust1.bank)

# for bank in cust2.bank:
#     print(bank.code)


# acct1 = Saving(23456729803, 2000)
# acct2 = Current(2416387892)

# cust1.request_loan(3000, 3425674356)
# cust1.request_loan(5000, 3425674356)

# first_bank.approve_loan(3425674356)
# first_bank.approve_loan(3425674356)


# for acct in cust1.account:
#     if acct.number == 3425674356:
#         print(acct.balance)
#         print(acct.book_balance)
#         print(acct.loans)

# print(first_bank.loans)
