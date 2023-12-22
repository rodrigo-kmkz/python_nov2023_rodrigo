a = float(input('ingrrese numero :'))
b = float(input('ingrese  numero :'))
c = float(input('ingrrese numero :'))
d = float(input('ingrese  numero :'))
e = float(input('ingrrese numero :'))

acu = 0
acu1 = 0
acu2 = 0
acu3 = 0
lista = [a, b, c, d, e]
prom = 0

x = len(lista)
print(f' la lista de numeros ingresados es {lista}  y la longitud de la lista es {x}')
for i in range(x):
    if lista[i] % 2 == 0:
        acu += 1
    else:
        acu1 = acu1 + 1
    if lista[i] >  0:
        acu2 = acu2 + 1
    else:
        acu3 = acu3 + 1
    
    prom = prom + lista[i]
    
print(f'de los numeros de la lista son pares  {acu} y los impares son {acu1}')


