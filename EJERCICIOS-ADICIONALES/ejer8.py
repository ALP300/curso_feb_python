'''
Sumar todos los elementos 
de un array
Crea un programa que tome una 
lista de números 
y calcule la suma de todos
sus elementos.
'''
numeros=[1,12,13,54,35,16,7,8,9,10,11,12]
suma=0
for i in numeros:
    suma+=i
print(f"La lista de números es: {numeros}")
print(f"La suma de los números es: {suma}")