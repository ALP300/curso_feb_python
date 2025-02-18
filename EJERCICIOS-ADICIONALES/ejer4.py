'''

Ejercicio

Escribir un programa que pida al usuario un 
número entero y muestre por pantalla un triángulo
rectángulo como el de más abajo, de altura
el número introducido.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
altura= int(input("Por favor ingresa la altura: "))
for i in range(1,altura+1,2):
    for j in range(i,0,-2 ):
        print(j, end=" ")
    print(" ")
    
