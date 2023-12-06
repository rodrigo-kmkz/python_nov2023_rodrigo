'''Recibir un valor de punto flotante con dos números decimales. Este valor representa un 
valor monetario. Luego de esto, calcular el menor numero posible de billetes y monedas en 
los cuales su valor puede ser descompuesto. Los billetes a tener en cuenta son de 100, 50, 
20, 10, 5, 2. Las monedas posibles son de 1, 0.50, 0.25, 0.10, 0.05 y 0.01. Mostrar el mensaje

"NOTAS:" seguido de una lista de billetes y el mensaje "MOEDAS:" seguido de una lista de monedas.

Entrada
El archivo de entrada contiene un valor de punto flotante N (0 ≤ N ≤ 1000000.00).

Salida
Mostrar la mínima cantidad de billetes y monedas necesarias para cambiar el valor inicial, como en el ejemplo dado.'''


dolares = float(input('dolares en billetes               :'))
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

dos = e // 2
do = e % 2 
print(f'numero de billetes de  2  = {dos} y sobra {do}')

mon1 = do // 1
mon = do % 1 
print(f'numero de monedas  de  1  = {mon1} y sobra {mon} ')

mon_05 = mon // 0.50
mon05 = mon % 0.50 
print(f'numero de monedas  de  0.50  = {mon1} y sobra {mon} ')

mon25 = mon05 // 0.25
mon_25 = mon05 % 0.25 
print(f'numero de monedas de  0.25  = {mon25} y sobra {mon_25} ')
