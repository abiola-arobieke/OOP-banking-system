from bank import Bank
from atm import Atm

first_bank = Bank('80078', 'Onikan, Lagos')

atm1 = Atm('Onikan, Lagos', first_bank)
atm2 = Atm('Onikan, Lagos', first_bank)

first_bank.add_atm(atm1)
first_bank.add_atm(atm2)

for atm in first_bank.atms:
    print(atm.location)
