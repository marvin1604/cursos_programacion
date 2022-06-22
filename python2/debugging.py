
def divisors(num):
    try:
        if num < 0:
            raise ValueError("ingresa un numero positivo")
        divisors= [i for i in range(1, num+1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    num = int(input("ingrese un numero: "))
    assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'
    print(divisors(int(num)))
    print("termino mi programa ")
    


if __name__ == "__main__":
    run()