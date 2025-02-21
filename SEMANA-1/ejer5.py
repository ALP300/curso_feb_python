'''
Calificación con letras
'''
calif= float(input("Ingrese la calificación: "))
if calif>=0 and calif<=100:
    if calif>=90:
        print("A")
    elif calif>=80:
        print("B")
    elif calif>=70:
        print("C")
    elif calif>=60:
        print("D")
    else:
        print("F")
else:
    print("Calificación inválida")