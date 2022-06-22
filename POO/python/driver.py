from account import Account

class Driver(Account):
    typeDriver = str

    def __init__(self, name, document, email, password, typeDriver):
        super().__init__(name, document, email, password)
        self.typeDriver = typeDriver