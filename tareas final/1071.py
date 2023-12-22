lista = []
num1 = int(input('Numero a ingresar :'))
num2 = int(input('Numero a ingresar :'))

acu = 0
for i in range((num1+1), (num2), 2):
    if (i) % 2 == 1:
        lista.append(i)
        print(lista , ' la I es = ', i )
        acu = acu + i
    
print(f'la suma de los imapres entre {num1} y {num2} = {acu}')

