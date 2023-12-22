
m = "SI"
while m == "SI" or m == "si":
    n1 = float(input('ingrese nota 1 ... : '))
    if n1 >=0 and n1 <= 10:
        n2 = float(input('ingrese nota 2 ... : '))
        if n2 >= 0 and n2 <= 10:
            n3 = float(input('ingrese nota 3 ... : '))
            if n3 >= 0 and n3 <= 10:
                n4 = float(input('ingrese nota 4 ... : '))
            else:
                print("Invalida, nota esta fuera del rango   ...")
        else:
            print("Invalida, nota esta fuera del rango   ...")
    else:
        print("Invalida, nota esta fuera del rango   ...")
    
    n11 = float("{0:.1f}".format(n1))
    n22 = float("{0:.1f}".format(n2))
    n33 = float("{0:.1f}".format(n3))
    n44 = float("{0:.1f}".format(n4))
    prom = (n11*2 + n22*3 + n33*4 + n44)/10
    print(" promedio de las notas obtenidas   = " , prom)
    if prom >= 7:
        print(" ALUMNO APROBADO ...")
    elif prom >= 5 and prom < 7:
        print(" ALUMNO SUPLETORIO ...")
        n5 = float(input('ingrese nota supletorio ... : '))
        n55 = float("{0:.1f}".format(n5))
        nuevoprom = (prom + n55)/2
        if nuevoprom >= 5:
            print(f"ALUMNO APROBADO nota del supletorio  =  {n55} y el promedio es {nuevoprom} ")
        else:  
            print(" ALUMNO REPROBADO ...", nuevoprom)
    elif prom < 5:
        print(" ALUMNO REPROBADO ...")
        
    m = input('desea continuar ingresar mas notas   ... SI / NO :')



