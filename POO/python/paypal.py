from payment import Payment

class Paypal(Payment):
    email   = str

    def __init__(self, amount, kind, email):
        super().__init__(amount, kind)
        self.email = email