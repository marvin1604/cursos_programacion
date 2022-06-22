from account import Account

class User(Account):
    typeUser = str

    def __init__(self, name, document, email, password, typeUser):
        super().__init__(name, document, email, password)
        self.typeUser = typeUser