'''En este problema, la tarea consiste en leer un código de un producto 1, el número de 
unidades del producto 1, el precio de una unidad de producto 1, el código de un producto 
2, el número de unidades del producto 2 y el precio de una unidad de producto 2. Después 
de esto, calcular y mostrar la cantidad a pagar.

Entrada
El archivo de entrada contiene dos líneas de datos. En cada línea habrá 3 valores: Dos enteros 
y un valor flotante con 2 dígitos después del punto decimal.

Salida
El archivo de salida debe ser un mensaje como en el siguiente ejemplo. Recuerde el espacio antes 
de ":" y antes del símbolo "R$". El valor debe ser presentado con 2 dígitos después del punto.'''

producto1 = (input('el codigo del producto   :'))
num_unidades1 = int(input('numero de unidades del producto   :'))
precio1 = float(input('precio * unidad producto  :'))
producto2 = (input('el codigo del producto   :'))
num_unidades2 = int(input('numero de unidades del producto   :'))
precio2 = float(input('precio * unidad producto  :'))

cuenta = num_unidades1*precio1 + num_unidades2*precio2


print(f'el cliente debe pagar ----->  $  {cuenta} ')




