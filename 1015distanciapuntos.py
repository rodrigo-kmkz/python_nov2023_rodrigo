'''Leer los cuatro valores correspondientes a las coordenadas x e y de dos puntos en el plano, 
p1 (x1, y1) y p2 (x2, y2) y calcular la distancia entre ellos, mostrando cuatro decimales después
del punto, de acuerdo a la fórmula:

Distancia = 

Entrada
La entrada contiene dos líneas de datos, la primera contiene dos valores double: x1 y1, la segunda 
también contiene dos valores double con un dígito después del punto: x2 y2.

Salida
Calcular y mostrar el valor de la distancia usando la fórmula provista, con 4 dígitos después del punto.'''

x1 = float(input('ingrese eje x  P1  x1   : '))
y1 = float(input('ingrese eje y  P1  y1   : '))
x2 = float(input("ingrese eje x  P2  x2   : "))
y2 = float(input("ingrese eje y  P2  y2   : "))

distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(f'distancia entre los puntos ingresados es :  {distancia}')
