'''Dos autos (X e Y) parten en la misma dirección. El auto X parte con una velocidad constante de 60 km/h 
y el auto Y parte con velocidad constante de 90 km/h.

En una hora (60 minutos), el auto Y se separa una distancia de 30 kilómetros del auto X, en otras palabras,
se aleja un kilómetro cada 2 minutos.

Leer la distancia (en kilómetros) y calcular que tiempo le lleva (en minutos) al auto Y tomar esa distancia
en relación con el otro auto.

Entrada
La entrada contiene 1 valor entero.

Salida
Imprimir el tiempo necesario seguido del mensaje "minutos", tal como se muestra en el ejemplo.'''
distanciakmX = int(input('distancia recorrida en km del auto x  :'))
distanciakmY = distanciakmX * 1.5
print(f' distancia recorrida por el auto Y =  {distanciakmY}  kilometros')
print(f'diferencia en kilometros de los dos autos {distanciakmY-distanciakmX}')


