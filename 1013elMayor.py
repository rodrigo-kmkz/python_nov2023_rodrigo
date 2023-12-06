'''Hacer un programa que lea 3 valores enteros y presente el mas grande seguido del mensaje 
"eh o maior". Usando la siguiente fórmula.



Entrada
El archivo de entrada contiene 3 valores enteros.

Salida
Imprimir el mas grande de los 3 valores seguido por un espacio y el mensaje "eh o maior".'''


A = float(input("ingrese el primer numero   : "))
B = float(input("ingrese el segundo numero  : "))
C = float(input("ingrese el tercero numero  : "))

if A > B and A > C:
    print(f" el primer numero es el mayor : {A}")
else:
    if B > C and B > A:
        print(f" el segundo numero es el mayor : {B}")
    else:
        if C > A and C > B:
            print(f" el tercer numero es el mayor : {C}")
        else:
            print(f" al menos 2 numeros son iguales ,   vuelva a ingresar numeros")





