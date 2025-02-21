'''
8️⃣ Adivina la Película 🎬
Dale pistas al usuario hasta que 
adivine la película correcta.

'''
import random
peliculas={
    'Dexter Morgan':'Película de un psicópata forense',
    'Harry Potter':'Película de magos',
    'Gladiador':'Película de un general romano',
    'Tetris':'Película de un juego de video',
    'Crepúsculo':'Película de vampiros',
    'La Sirenita':'Película de una sirena',
    'Flow ':'Película de un gato, en una inundacion',
    'El Rey León':'Película de leones',
    'El Padrino':'Película de la mafia',
    'Rapido y Furioso':'Película de carreras',
}
peliculas,pista= random.choice(list(peliculas.items()))
print(f"Pista {pista}")

while True:
    respuesta=input("¿Cuál es la película?: ")
    if respuesta==peliculas:
        print("¡Correcto!")
        break
    else:
        print("¡Incorrecto! Inténtalo de nuevo.")