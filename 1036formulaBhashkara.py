'''Leer 3 números de punto flotante. Luego, imprimir las raíces de la fórmula de Bhaskara. 
Si es imposible calcular las raíces debido a una división por cero ó a la raíz cuadrad de 
un número negativo, presentar el mensaje “Impossivel calcular”.

Entrada
Leer 3 números de punto flotante (double) A, B y C.

Salida
Mostrar el resultado con 5 dígitos luego del punto decimal ó el mensaje si es imposible de calcular.'''

A = float(input("ingrese el primer numero:  "))
B = float(input("ingrese el segundo numero: "))
C = float(input("ingrese el tercer numero:  "))




if A == 0 or B == 0 or C == 0:
    print('imposible calcular el resultado ')
else:
    r_pos = ((-B + (B**2-(4*A*C))**(1/2))/(2*A))
    r_neg = ((-B - (B**2-(4*A*C))**(1/2))/(2*A))
    x = (B**2-(4*A*C))**(1/2)
    y = -B + x
    w = -B - x
    z = y / (2*A)
    zz = w / (2*A)
    print("la respuesta positiva de la formula es  {0:.5f}".format(r_pos))
    print("la respuesta negativa de la formula es  {0:.5f}".format(r_neg))
    
    
    