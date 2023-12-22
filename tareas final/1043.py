z = "S"
while z == 'S' or z == 's':
    a = float(input('ingrese numero 1 ... : '))
    b = float(input('ingrese numero 2 ... : '))
    c = float(input('ingrese numero 3 ... : '))
    if (a+b) > c:
        perimetro = a + b + c
        print('perimetro del triangulo es igual a : ' , perimetro)
    else:
        areaTrapecio = c*((a+b)/2)
        print(f'area del trapecio  =  {areaTrapecio:.1f}'.format(areaTrapecio))
    z = input(" desea continuar en el programa S o N   " )       


