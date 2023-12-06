'''En este problema tienes que leer un valor entero y calcular el menor número posible de billetes 
en que puede ser descompuesto. Los billetes posibles son 100, 50, 20, 10, 5, 2 y 1. Imprimir el 
valor leído y la lista de billetes.

Entrada
La entrada contiene un valor entero N (0 < N < 1000000).

Salida
Imprimir el número leído y la cantidad mínima necesaria de billetes en lenguaje portugués, 
como muestra el ejemplo. No olvides imprimir el final de línea luego de cada línea, de otra forma 
recibirás “Presentation Error”.'''

dolares = int(input('dolares en billetes               :'))
cien = dolares // 100
c = dolares % 100
print(f'numero de billetes de 100 = {cien}  y sobra  {c}')

cincuenta = c // 50
cc = c % 50
print(f'numero de billetes de  50 = {cincuenta}  y sobra {cc}')

veinte = cc // 20
v = cc % 20
print(f'numero de billetes de  20 = {veinte}  y sobra {v}')

diez = v // 10
d = v % 10 
print(f'numero de billetes de  10 = {diez}  y sobra {d}')

cinco = d // 5
e = d % 5 
print(f'numero de billetes de  5  = {cinco}  y sobra {e}')

uno = e // 5
u = e % 5 
print(f'numero de billetes de  1  = {e} ')



