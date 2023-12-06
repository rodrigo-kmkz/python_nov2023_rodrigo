'''Escribe un programa que lea un número de empleado, su número de horas trabajadas en el mes 
y el monto recibido por hora. Imprimir el número de empleado y el salario que él/ella recibirá 
a fin de mes, con dos lugares decimales.

No se olvide de imprimir los saltos de líneas después del resultado, de lo contrario, 
recibirá “Presentation Error”.
No se olvide del espacio en blanco antes y después del signo igual y después de U$.
Entrada
El archivo de entrada contiene 2 números enteros y 1 valor de punto flotante, representando 
el número, cantidad de horas trabajadas y el monto recibido del empleado por hora trabajada.

Output
Imprimir el número y salario del empleado, acorde al siguiente ejemplo, con los espacios en 
blanco antes y después del signo igual.'''

numero = int(input('numero empleado   :'))
horas = int(input('Horas trabajadas  :'))
pagoHoras = int(input('Pago horas   $ :'))

sueldo  = horas * pagoHoras

print(f'el empleado --> {numero} : recibe el sueldo de $. {sueldo}')
