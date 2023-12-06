'''Timelimit: 1
Escriba un programa que lea tres valores de punto flotante: A, B y C. Luego, calcular y mostrar:
a) El área del triángulo rectángulo de base A y altura C.
b) El área del círculo de radio C (Pi = 3.14159).
c) El área del trapecio el cual tiene A y B como bases, y C como altura.
d) El área del cuadrado de lado B.
e) El área del rectángulo de lados A y B.

Entrada
La entrada contiene tres valores de doble precisión con un dígito luego del punto decimal.

Salida
La salida contiene 5 renglones. Cada uno de los renglones corresponde a las áreas
descriptas anteriormente, siempre con el mensaje correspondiente (en portugués) y 
un espacio entre los dos puntos y el valor. El valor calculado debe ser presentado 
con 3 dígitos luego del punto decimal.
'''
A = float(input("ingrese el primer numero: "))
B = float(input("ingrese el segundo numero: "))
C = float(input("ingrese el tercero numero: "))
pi = 3.14159
triangulo = (A*C)/2
print(f'el area del triangulo es  (A*C)/2 = {triangulo} metros')
area_circ = pi * C**2
print(f'el area del area del circulop es pi * C**2 =   {area_circ} metros cuadrados ')
area_trapecio = ((A + B)/2)*C
print(f'el area del trapecio es      :   ((A + B)/2)*C = {area_trapecio} metros cuadrados ')
area_cuadrado = B**2
print(f'el area del cuadrado  es     :   B**2          = {area_cuadrado} metros cuadrados ')
area_rectangulo = (A*B)/2
print(f'el area del rectangulo   es  :   (A*B)/2       = {area_rectangulo} metros cuadrados ')







