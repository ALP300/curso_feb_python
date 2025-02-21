'''
 Crear una tabla de multiplicar Escribe un programa que 
 pida un número al usuario y genere su tabla de 
 multiplicar del 1 al 10.usando un bucle
'''
num= int(input("Ingrese un número: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")