num1 = int(input('numeros a ingresar :'))
acu = 0
pot = 0
for i in range(num1):
    if i%2 == 1:
        pass
    else: 
        pot = i**2
        acu = acu + pot
        print(f'{i} a la potencia 2  = {pot}')
