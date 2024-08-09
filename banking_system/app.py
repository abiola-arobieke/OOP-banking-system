from bank import Bank
from account import Saving, Current

first_bank = Bank('80078', 'Onikan, Lagos')

saving_acct = Saving(3132424269)
current_acct = Current(3234227820, 50)

first_bank.add_account(saving_acct)
first_bank.add_account(current_acct)


for account in first_bank.accounts:
    print(f"Account no: {account.number}, Acccount balance: {account.balance}")

print(saving_acct.bank.code)
print(current_acct.bank.code)
