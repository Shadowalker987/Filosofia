# juego_adivinanza.py

import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza de números!")
    print("Estoy pensando en un número entre 1 y 100.")

    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        # Solicitar al jugador que ingrese un número
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        intentos += 1

        # Comprobar la adivinanza
        if adivinanza < numero_secreto:
            print("El número es mayor.")
        elif adivinanza > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    juego_adivinanza()
