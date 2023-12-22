listaIN = []
listaOUT = []
listaTOT = []
num1 = int(input('cantidad de numeros a ingresar :'))
acu = 0
acu1 = 0
for i in range(num1):
    num2 = int(input(f'numeros a ingresar {i}  :'))
    if num2 < 10 or num2 >20 : 
        listaIN.append(num2)
        acu = acu + 1
        
    else :
        listaOUT.append(num2)
        acu1 = acu1 + 1
    listaTOT.append(num2)    
print(listaIN , f' son los numeros FUERA del rango (10 a 20)   {acu1} \n')    
print(listaOUT , f' son los numeros DENTRO del rango (10 a 20)   {acu} \n')
print(f'los numeros ingresados son  {listaIN} + {listaOUT}\n')
print(f'los numeros ingresados son  {listaTOT}')


