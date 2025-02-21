'''
Verificar divisibilidad por 3 y 5
'''
num = int(input("Ingrese un número: "))
if num%3==0 and num%5==0:
    print(f"{num} es divisible por 3 y 5")
elif num%3==0:  
    print(f"{num} es divisible por 3")
elif num%5==0:
    print(f"{num} es divisible por 5")
else:
    print(f"{num} no es divisible por 3 ni por 5")