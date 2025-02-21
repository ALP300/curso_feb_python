'''
LISTAS, TUPLAS Y DICCIONARIOS
'''

'''
#LISTAS
canasta=['manzana','pera','naranja','uva']
ubicacion= int(input("¿Qué fruta buscas?: "))

print(canasta[ubicacion])
print(canasta[-2])
print(canasta[1:3])
print(canasta[1:])
print(canasta[:3])
print(canasta[0:4])
print(canasta)

def agregar_fruta(fruta):
    canasta.append(fruta)
    print(canasta)

def eliminar_fruta(frut):
    canasta.remove(frut)
    print(canasta)
    
fruta= input("Ingresa la fruta a agregar: ")
frut= input("Ingresa la fruta a eliminar: ")
agregar_fruta(fruta)
eliminar_fruta(frut)

'''
tupla= ('manzana','pera','naranja','uva','uva','uva','uva','uva','uva')
def mostrar_tupla():
    return tupla

def buscar_tupla():
    fruta= input("¿Qué fruta buscas?: ")
    if fruta in tupla:
        print("¡Sí está!")
    else:
        print("No está")

def contar_tupla(elemento):
    return tupla.count(elemento)

fruta= input("Ingresa la fruta a buscar repeticiones: ")
buscar_tupla()
print(contar_tupla(fruta))
print(mostrar_tupla())