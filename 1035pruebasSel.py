'''Leer 4 valores enteros A, B, C y D. Luego, si B es mayor que C, D es mayor que A, la suma 
de C y D es mayor que la suma de A y B, C y D son valores positivos y A es par, escribir el 
mensaje “Valores aceitos” (Valores aceptados). De lo contrario, escriba el mensaje “Valores 
nao aceitos” (Valores no aceptados).

Entrada
Cuatro números enteros A, B, C y D.

Salida
Mostrar el mensaje correspondiente luego de la validación de los números.'''

A = int(input("ingrese el primer numero:  "))
B = int(input("ingrese el segundo numero: "))
C = int(input("ingrese el tercer numero:  "))
D = int(input("ingrese el cuarto numero:  "))

if B>C and D>A and (C+D)>(A+B) and C >= 0 and D >= 0 and A%2==0:
    print('VALORES ACEPTADOS')
else:
    print('VALORES no ACEPTADOS')
    

