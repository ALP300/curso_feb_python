'''
4. Contar números pares e impares en un array
'''
numeros= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16,17,18,19,20]
pares=[]
impares=[]
for i in numeros:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)

print(f"La lista de números es: {numeros}")
print(f"La lista de números pares es: {pares}")
print(f"La lista de números impares es: {impares}")