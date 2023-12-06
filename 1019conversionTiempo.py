''' Leer un valor entero, que es la duración en segundos de un evento realizado en una fábrica, 
e informarlo expresado en horas:minutos:segundos.

Entrada
El archivo de entrada contiene al entero N.

Output
Imprimir el tiempo leído del archivo de entrada (segundos) convertido en horas:minutos:segundos 
como el ejemplo siguiente.'''

segundos = int(input('Numero entero en segundos    : '))
seg = segundos % 60
minutos = segundos // 60
min =  minutos % 60
horas = minutos // 60

print (f" conversion final horas minutos segundos   =  {horas} ' : '  {min}  ' : '  {seg}")




