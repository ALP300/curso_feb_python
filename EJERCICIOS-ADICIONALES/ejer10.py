'''
1️⃣ Adivina el Número (con pistas) 🎯
Escribe un programa que elija un número 
aleatorio entre 1 y 100. El usuario debe
adivinarlo y recibir pistas como 
"más alto" o "más bajo".
'''
import random
numero= random.randint(1,100)

intentos=0
print("Adivina el número entre 1 y 100")

while True:
    intento= int(input("Introduce un número: "))
    intentos+=1
    if intento<numero:
        print("Más alto")
    elif intento>numero:
        print("Más bajo")
    else:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break