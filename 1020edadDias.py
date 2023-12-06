'''Leer un entero, que corresponde a la edad de una persona (en días) e imprimirlo en años,
meses y días, seguido del respectivo mensaje “ano(s)”, “mes(es)”, “dia(s)”.

Nota: Para facilitar el cálculo, considere al año con 365 días y al mes con 30. En los casos 
de prueba nunca habrá una situacion que permita 12 meses y algunos días, como 360, 363 ó 364. 
Este es sólo un ejercicio para plantear un simple razonamiento matemático.

Entrada
La entrada consiste en un solo valor entero.

Salida
Mostrar el resultado, como se muestra a continuación.'''

edad = int(input('ingrese edad en dias              : '))
anos = edad // 365
anos1 = edad % 365

mes = anos1 // 30
mes1 = anos1 % 30

print (f" conversion final dias meses anos --->  anos : {anos}  mes : {mes}  dias {mes1}")


