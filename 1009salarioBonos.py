'''Timelimit: 1
Escriba un programa que lea el nombre de un vendedor, su salario fijo y el total de las 
ventas realizadas por él en el mes (en dinero). Considerando que el vendedor recibe un 15% 
de los productos vendidos, escribir el salario final (total) de cada vendedor a fin de mes, 
con dos cifras decimales.

- No olvide de imprimir un final de linea luego del resultado, de otra forma recibirá “Presentation Error”.

- No olvide los espacios en blanco.

Entrada
La entrada contiene un texto (primer nombre del empleado), y dos valores de doble precisión, 
los cuales representan el salario del vendedor y el valor total vendido por él.

Salida
Imprimir el salario total del vendedor, de acuerdo a los ejemplos.'''


vendedor = (input('nombre del vendedor  :'))
salario = int(input('salario vendedor   :'))
ventas = int(input('ventas realizadas   :'))

salario1 = salario + (ventas * 0.15)

print(f'el empleado --> {vendedor} : recibe el sueldo total de $. {salario1}')


