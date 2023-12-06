'''Leer tres valores (variables A, B y C), que son las tres notas de estudiantes. Entonces, calcule el promedio, 
considerando que la nota A tiene peso 2, la nota B tiene peso 3 y la nota C tiene peso 5. Cosiderar que cada nota
puede ser del 0 al 10.0, siempre con un punto decimal.

Entrada
El archivo de entrada contiene 3 valores de punto flotante (double) con un dígito decimal después de la coma.

Salida
Imprime el mensaje "MEDIA"(Promedio en Portugués) y el promedio de los estudiantes de acuerdo con el siguiente 
ejemplo, con un espacio en blanco antes y después del signo igual.'''



A = float(input("ingrese el primer numero: "))
B = float(input("ingrese el segundo numero: "))
C = float(input("ingrese el tercero numero: "))
if A >= 0 and A <= 10 and B >= 0 and B <= 10 and C >= 0 and C <= 10:
    aa = (A * 2)/10
    bb = (B * 3)/10
    cc = (C * 5)/10
    promedio2 = (aa + bb + cc)
    print(f'el promedio de las 3 notas de los estudiantes es  {aa} , {bb} y {cc} = {promedio2}')
else:
    print('notas no son validas deben ser entre 0 y 10')
    
    
    
