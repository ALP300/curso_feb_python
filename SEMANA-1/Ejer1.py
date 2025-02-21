'''
Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).

'''
num1= float(input("Ingrese el primer número: "))
num2= float(input("Ingrese el segundo número: "))
suma= num1+num2
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {num1-num2}")
print(f"La multiplicación de {num1} y {num2} es: {num1*num2}")
print(f"La división de {num1} y {num2} es: {num1/num2}")
print(f"La división entera de {num1} y {num2} es: {num1//num2}")
print(f"El residuo de {num1} y {num2} es: {num1%num2}")

