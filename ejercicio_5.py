# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def caculoAnio(anio):
    
    if anio %100 != 0 and anio  % 4 == 0 or  anio  % 400 == 0:
        print("El años es bisiesto")
    else :
       print("EL año no es bisiesto")



anio = int ( input("inrese un año : "))

caculoAnio(anio)


