from bank import Bank
from atm import Atm
from customer import Customer

first_bank = Bank('80078', 'Onikan, Lagos')
gt_bank = Bank('80456', 'Berger, Lagos')

cust1 = Customer('Van Persie', 'Surulere, Lagos')
cust2 = Customer('John Travola', 'Ojodu, Lagos')

first_bank.create_account(cust1, 3425674356, 4500)
gt_bank.create_account(cust1, 2352789123)
first_bank.create_account(cust2, 4352789123)


atm1 = Atm('Onikan, Lagos', first_bank)
atm1.deposit(50000)
# atm2 = Atm('Onikan, Lagos', first_bank)

first_bank.add_atm('Dugbe, Ibadan')
first_bank.add_atm('Challenge, Ibadan')

for account in cust1.account:
    if account.number == 3425674356:
        account.withdraw(1000, atm1)
        print(account.balance)
