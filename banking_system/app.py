from bank import Bank
from atm import Atm
from account import Current, Saving
from transaction import Transaction

first_bank = Bank('80078', 'Onikan, Lagos')

acct1 = Saving(23456729803)
acct2 = Current(2416387892)

atm1 = Atm('Onikan, Lagos', first_bank)
atm2 = Atm('Onikan, Lagos', first_bank)

tran1 = Transaction(3000, acct1, atm1)
tran1 = Transaction(5000, acct1, atm1)

print(acct1.transaction)
print(atm1.transaction)
