from bank import Bank
from account import Saving, Current
from customer import Customer

first_bank = Bank('80078', 'Onikan, Lagos')

saving_acct = Saving(3132424269)
current_acct = Current(3234227820, 50)

first_bank.add_account(saving_acct)
first_bank.add_account(current_acct)

cust1 = Customer('Van Persie', 'Surulere, Lagos')


for account in first_bank.account:
    print(f"Account no: {account.number}, Acccount balance: {account.balance}")

print(saving_acct.bank.code)
print(current_acct.bank.code)


cust1.add_account(saving_acct)
cust1.add_account(current_acct)

print(saving_acct.customer.name)
