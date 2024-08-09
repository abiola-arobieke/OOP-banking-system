class Customer:

    def __init__(self, name, address, password=None, card_number=None, pin=None):
        self.name = name
        self.address = address
        self.password = password
        self.card_number = card_number
        self.pin = pin

    def verify_password(self):
        pass
    


    