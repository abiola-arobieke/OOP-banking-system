from bank import Bank
from atm import Atm
from account import Current, Saving
from transaction import Transaction

first_bank = Bank('80078', 'Onikan, Lagos')

acct1 = Saving(23456729803, 2000)
acct2 = Current(2416387892)

atm1 = Atm('Onikan, Lagos', first_bank)
atm2 = Atm('Onikan, Lagos', first_bank)
