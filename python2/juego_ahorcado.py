import os
import random

os.system("clear")

def choice_word():
    with open("./data.txt", "r", encoding="utf-8") as f:
        words = [i.replace('\n', '') for i in f]
        return random.choice(words)


def run():
    guess = choice_word().lower()
    guess = guess.replace('á', 'a')
    guess = guess.replace('é', 'e')
    guess = guess.replace('í', 'i')
    guess = guess.replace('ó', 'o')
    guess = guess.replace('ú', 'u')

    intentos = ['♥' for i in range(0, 10)  ]
    secret_word = ["-" for i in range(0, len(guess))]

    while(len(intentos) > 0):
        word_added = False
        try:
            print('_____________________')
            print(" ".join(intentos))    
            print("¡Adivina la palabra!\n")
            print(" ".join(secret_word))
            letter = input("\nIntroduce una letra: ").lower()
            os.system("clear")
            if letter.isnumeric() or len(letter) != 1:
                raise ValueError
            for index, letter_guess in enumerate(guess):
                if letter == letter_guess:
                    secret_word[index] = letter
                    word_added = True
            if word_added == False:
                    intentos.pop()
            if "".join(secret_word) == guess:
                print('\n_____________________')
                print(" ".join(intentos))
                print("\n" + "  ".join(secret_word))
                print('\nLo lograste')
                break
        except ValueError:
            if letter.isnumeric():    
                print("No hay números en esta palabra")
                intentos.pop()
            elif len(letter) >= 1:
                print("Debes ingresar una letra a la vez")
                intentos.pop()
            elif len(letter) == 0:
                print("Debes ingresar al menos una letra ")
                intentos.pop()
    if len(intentos) == 0:
        print('\n_____________________')
        print(" ".join(intentos))
        print("Se acabaron los intentos, la palabra correcta era:\n \n" + " ".join(guess))

if __name__ == "__main__":
    run()