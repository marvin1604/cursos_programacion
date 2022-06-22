from payment import Payment

class Efectivo(Payment):
    entry    = int
    exchange = int

    def __init__(self, amount, kind, entry, exchange):
        super().__init__(amount, kind)
        self.entry    = entry
        self.exchange = exchange