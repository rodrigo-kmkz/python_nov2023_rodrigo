'''Debes hacer un programa que lea un número de punto flotante e imprimir un mensaje 
diciendo en cuál de los siguientes intervalos el número pertenece: [0,25] (25,50], 
(50,75], (75,100). Número es menor que cero o mayor que 100, el programa debe imprimir
el mensaje "Fora de intervalo" que significa "Fuera de intervalo".

Entrada
El archivo de entrada contiene un número de punto flotante.

Salida
La salida debe ser un mensaje como el siguiente ejemplo.'''

a = float(input("ingrese el numero:  "))
if a >= 0 and a<=25:
    print('numero ingresado esta en el primer rango  a >= 0 and a <= 25 ')
else:
    if a > 25 and a <= 50:
        print('numero ingresado esta en el segundo rango a > 25 and a <= 50 ')
    else:
        if a > 50 and a <= 75:
            print('numero ingresado esta en el tercer rango   a > 50 and a <= 75 ')
        else:
            if a > 75 and a < 100:
                print('numero ingresado esta en el cuarto  rango   a > 75 and a < 100 ')
            else:
                print('numero ingresado esta fuera del intervalo ........')


