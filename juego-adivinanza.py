
import random

numero_secreto = random.randint(1, 100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenide al juego de adivinar el número secreto! Tenés 5 intentos para adivinarlo.")

while not adivinado and cant_intentos < cant_max_intentos:
    numero = int(input("Adiviná el número secreto entre 1 y 100: "))
    if numero == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        adivinado = True
    elif numero < numero_secreto:
        print("El número secreto es mayor que", numero)
    else:
        print("El número secreto es menor que", numero)

    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("¡Ups! agotaste tus intentos. El número secreto era:", numero_secreto)
