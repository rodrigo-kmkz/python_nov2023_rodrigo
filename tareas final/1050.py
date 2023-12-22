'''Lea un número entero que corresponda al número de código de área para marcación telefónica. 
A continuación, imprima el destino de acuerdo con la siguiente tabla:

Si el número de entrada no se encuentra en la tabla anterior, la salida debe ser:
DDD nao cadastrado
Que significa “DDD no encontrado” in Portugues.

Entrada
La entrada consiste en un único número entero.

Salida
Imprima el nombre de la ciudad correspondiente a la entrada DDD. Imprimir DDD nao cadastrado si no existe DDD correspondiente al número ingresado.'''

ddd = [61,71,11,21,32,19,27,31]
destino = ['brasilia' , 'salvador', 'sao paolo', 'rio de janeiro','juiz de fora', 'campinas' ,'victoria','belo horionte']

num = int(input('INGRESE EL DDD deseado :  '))
a = len(ddd)
if num in ddd:
    for aa in range(a):
        if ddd[aa] == num:
            print(f' codigo DDD {ddd[aa]} corresponde destino {destino[aa]}')
else:
    print('codigo DDD INVALIDO...')






