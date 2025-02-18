'''
Ejercicio 7
Escribir un programa que cree un diccionario 
simulando una cesta de la compra. El programa 
debe preguntar el artículo y su precio y añadir 
el par al diccionario, hasta que el usuario decida 
terminar. Después se debe mostrar por pantalla la
lista de la compra y el coste total, 
con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste

'''
cesta={}
continuar= True
while continuar:
    articulo= input("Por favor ingresa un artículo: ")
    precio= float(input("Introduce el precio de "+articulo+" : "))
    cesta[articulo]= precio
    continuar= input("¿Quieres añadir más artículos (Si/No)? ")=="Si"
coste=0
print("Lista de compra: ")
for articulo, precio in cesta.items():
    print(articulo,'\t', precio)
    coste+=precio

print("Coste total: ",coste)
    