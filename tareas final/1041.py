x = float(input('ingrese valor de eje X ... : '))
y = float(input('ingrese valor de eje Y ... : '))

if x == 0 and y == 0:
    print(' el punto ingresado esta en el origen del plano cartesiano...')
elif x > 0 and y > 0:
    print(" el punto ingresado esta en el cuadrante 1 +X y +Y ")
elif x < 0 and y < 0:
    print(" el punto ingresado esta en el cuadrante 3 -X y -Y ")
elif x > 0 and y < 0:
    print(" el punto ingresado esta en el cuadrante 2 +X y -Y ")
elif x < 0 and y > 0:
    print(" el punto ingresado esta en el cuadrante 4 -X y +Y ")
else:
    print(" uno de los ejes esta en eje como punto 0 ")
