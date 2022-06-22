import random
import os

os.system("clear")

def palabra_aleatoria():
    with open("./DATA.txt", "r", encoding="utf-8") as f:
        list=[i.strip() for i in f]
        return random.choice(list)

def run():
    
    palabra = palabra_aleatoria().lower()
    palabra = palabra.replace('á', 'a')
    palabra = palabra.replace('é', 'e')
    palabra = palabra.replace('í', 'i')
    palabra = palabra.replace('ó', 'o')
    palabra = palabra.replace('ú', 'u')

    palabra_secreta=["_" for i in range(len(palabra))]
    intentos = 0        

    while " ".join(palabra_secreta)  != " ".join(palabra):
        print("*"*166)
        print("-"*25, "ADIVINA LA PALABRA CORRECTA","-"*25)
        # print(palabra)
        print("\n")
        print(" "*15, "palabra escondida:"," ".join(palabra_secreta))
        print("\n")  
        print("""
           ******  *       *    *****  ******* *******    *
           *         *   *        *       *    *     *    *
           ***         *          *       *    *     *    *
           *         *   *        *       *    *     *
           ******  *       *    *****     *    *******    *
      
         """)
        print("Numero de intentos para ganar:   ", intentos) 
        letra=input("ingrese una letra:   ").lower()     
        os.system("clear")            
        
        for contador, letra2 in enumerate(palabra):
            
            if letra == letra2:
                palabra_secreta[contador] = letra2
        intentos += 1        

        
    if " ".join(palabra_secreta)  == " ".join(palabra):

        os.system("clear")
        print("*"*166)
        print("ganaste!!!!----"*50)
        print("*"*23,"LO LOGRASTE EN :  ", intentos, "INTENTOS","*"*23) 
        print("""
           ******  *       *    *****  ******* *******    *
           *         *   *        *       *    *     *    *
           ***         *          *       *    *     *    *
           *         *   *        *       *    *     *
           ******  *       *    *****     *    *******    *
      
      """)
        print("*"*166)
        print("-"*25, "HECHO POR WALTER RODRIGUEZ","-"*25)

      
if __name__ == "__main__":
    run()