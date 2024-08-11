from bank import Bank
from atm import Atm
from account import Current, Saving
from customer import Customer

first_bank = Bank('80078', 'Onikan, Lagos')
cust1 = Customer('Van Persie', 'Surulere, Lagos')

first_bank.create_account(cust1, 3425674356, 4500)

atm1 = Atm('Onikan, Lagos', first_bank)
atm2 = Atm('Onikan, Lagos', first_bank)

acct1 = Saving(23456729803, 2000)
acct2 = Current(2416387892)

cust1.request_loan(3000, 3425674356)
cust1.request_loan(5000, 3425674356)

first_bank.approve_loan(3425674356)
first_bank.approve_loan(3425674356)


for acct in cust1.account:
    if acct.number == 3425674356:
        print(acct.balance)
        print(acct.book_balance)
        print(acct.loans)

print(first_bank.loans)