from bank import Bank
from customer import Customer

first_bank = Bank('80078', 'Onikan, Lagos')

cust1 = Customer('Van Persie', 'Surulere, Lagos')

first_bank.create_account(cust1, 3132424759)
first_bank.create_account(cust1, 3234227820, 200, 'current')

for account in cust1.account:
    print(
        f"Acct no: {account.number}, Acct bal: {account.balance}, Acct Type: {account.type}"
    )
