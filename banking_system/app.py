from bank import Bank
from atm import Atm

first_bank = Bank('80078', 'Onikan, Lagos')

atm1 = Atm('Onikan, Lagos', first_bank)
atm2 = Atm('Onikan, Lagos', first_bank)

atm1.deposit(50000)
atm1.deposit(400000)

print(atm1.get_deposit())
print(atm1.balance)
