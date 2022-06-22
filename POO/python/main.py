from uberX import UberX
from account import Account
from car import Car
if __name__ == "__main__":
    print("hola mundo")
    uberX = UberX("AMS 234" , Account("andres herrera", "ANDA876", "walter.rodriguez1992@gmail.com", "12a4"), "toyota", "corolla")
    print(vars(uberX))
    print(vars(uberX.driver))


    # car2 = Car("QWE567", Account("martha", "ANDA123", "walter.rodriguez1992@gmail.com", "12a4"))
    # print(vars(car2))
    # print(vars(car2.driver))

