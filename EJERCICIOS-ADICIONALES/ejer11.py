'''
4️⃣ Juego de "Piedra, Papel o Tijera" ✊📄✂️
Juega contra la computadora en un duelo épico.

'''
import random
opciones=["piedra","papel","tijera"]
computadora= random.choice(opciones)
usuario= input("Piedra, papel o tijera: ").lower()
print(f"Computadora: {computadora}")
if usuario==computadora:
    print("¡Empate!")
elif (usuario=="piedra" and computadora=="tijera") or (usuario=="papel" and computadora=="piedra") or (usuario=="tijera" and computadora=="papel"):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")  