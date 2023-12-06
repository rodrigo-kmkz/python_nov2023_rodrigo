'''Leer dos valores enteros. Luego, calcular el producto entre ellos y guardar el resultado 
en una variable llamada PROD. Imprimir el resultado como se muestra en los ejemplos.
No olvides imprimir el final de línea luego del resultado, de otra forma recibirás “Presentation Error”.

Entrada
La entrada contiene dos números enteros.

Salida
Imprimir el mensaje "PROD" y PROD de acuerdo a los ejemplos, con un espacio antes y luego del signo igual.'''



A = int(input("ingrese el primer numero: "))
B = int(input("ingrese el segundo numero: "))

prod = A * B

print(f'PRODUCTO de los 2 numeros ingresados : {A} + {B} = {prod}')