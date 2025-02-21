'''
Ejercicio 10
Escribir un programa que permita gestionar la base de
datos de clientes de una empresa. Los clientes se
guardarán en un diccionario en el que la clave de
cada cliente será su NIF, y el valor será otro
diccionario con los datos del cliente (nombre, dirección, 
teléfono, correo, preferente), donde preferente tendrá el 
valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción 
del siguiente menú: (1) Añadir cliente, (2) Eliminar 
cliente, (3) Mostrar cliente, (4) Listar todos los 
clientes, (5) Listar clientes preferentes, (6) Terminar. 
En función de la opción elegida el programa tendrá que
hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario 
con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de
la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su 
NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos 
con su NIF y nombre.
Terminar el programa.
'''
clientes={}
opcion= ''
while opcion != '6':
    if opcion == '1':
        nif=input("Por favor ingrese el NIF del cliente: ")
        nombre=input("Por favor ingrese el nombre del cliente: ")
        direccion=input("Por favor ingrese la dirección del cliente: ")
        telefono=input("Por favor ingrese el teléfono del cliente: ")
        correo=input("Por favor ingrese el correo del cliente: ")
        preferente=input("Por favor ingrese si el cliente es preferente: ")
        clientes[nif]={'nombre':nombre, 'direccion':direccion, 'telefono':telefono, 'correo':correo, 'preferente':preferente}
    if opcion == '2':
        nif=input("Por favor ingrese el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("El cliente no existe")
    
    if opcion == '3':
        nif=input("Por favor ingrese el NIF del cliente: ")
        if nif in clientes:
            print('NIF', nif)
            for clave,valores in clientes[nif].items():
                print(clave,':',valores)
        else:
            print("El cliente no existe")
    
    if opcion== '4':
        print("Lista de clientes: ")
        for clave,valores in clientes.items():
                print(clave,':',valores)
            
    
    opcion= input("Por favor ingrese una opción del siguiente menú: \n(1) Añadir cliente, \n(2) Eliminar cliente, \n(3) Mostrar cliente,\n(4) Listar todos los clientes, \n(5) Listar clientes preferentes, \n(6) Terminar. ")