import time
print("Cargando...")
time.sleep(3)   #Esperar 3 segundos
pi = 3.14159265359
print("--------------------------------------------")
print("BIENVENIDO A LA MEJOR CALCULADORA GEOMETRICA")
print("-----CREADA POR EL MEJOR SER HUMANO, YO-----")
print("--------------------------------------------")

Figuras = None
seguir = "si"
while seguir == "si":
    try:    
        Figuras = int(input("Por favor digame en que figura lo puedo ayudar tenemos: \nFIGURAS 2D \n\n1.RECTANGULO \n2.CIRCULO \n3.TRAPECIO \n4.PARALELOGRAMO \n\nFIGURAS 3D \n\n5.PARALELEPIPEDO \n6.PRISMA RECTANGULAR \n7.CILINDRO \n8.ESFERA \n\n9.TRIANGULO RECTANGULO: \n\n"))
        if Figuras < 1 or Figuras > 9:
            print("Digito no disponible, vuelva a intentarlo")
            continue
    except (ValueError, NameError):
        print("Opcion invalida vuelva a intentarlo: ")   
        continue   

    if Figuras == 1:
        RECTANGULO = C_R = input("Porfavor dime que quieres calcular del Rectangulo te puedo hallar: \nArea (a) \nBase (b) \nAltura (h) \nPerimetro (p) ")
        if C_R == "a" or "Area":
            c_b1 = float(input("Porfavor necesito que me ingreses el dato de Base (b) ingreselo en decimal (float): "))
            c_h1 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_a1 = (c_b1 * c_h1)  
            print("El resultado del area es", r_a1)
        elif C_R == "b" or "Base":
            c_a2 = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            c_h2 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_b1 = (c_a2 / c_h2)
            print("El resultado de la base es", r_b1)
        elif C_R == "h" or "Altura":
            c_a3 = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            c_b3 = float(input("Porfavor necesito que me ingreses el dato de Base (b) ingreselo en decimal (float): "))
            r_h1 = (c_a3 / c_b3)
            print("El resultado de la Altura es",r_h1)
        elif C_R == "p" or "Perimetro":
            c_b4 = float(input("Porfavor necesito que me ingreses el dato de Base (b) ingreselo en decimal (float): "))
            c_h4 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_p1 = (c_b4 + c_h4) * 2
            print("El resultado del perimetro es",r_p1)
    
    if Figuras == 2:
        CIRCULO = C_C = input("Porfavor dime que quieres calcular del Circulo te puedo hallar: \nArea (a) \nRadio (r) \nCircunferencia (c): ")
        if C_C == "a" or "Area":
            c_r = float(input("Porfavor necesito que me ingreses el dato de Radio (r) ingreselo en decimal (float): "))
            r_a2 = (c_r ** 2) * pi 
            print("El resultado del area es",r_a2)
        elif C_C == "r" or "Radio":
            h_a = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            r_r2 = (h_a / pi)**(1/2)
            print("El resultado del radio es",r_r2)
        elif C_C == "c" or "Circunferencia":
            h_r = float(input("Porffavor necesito que me ingreses el dato de Radio (r) ingreselo en decimal (float):"))
            r_c = ((2 * pi) * h_r)
            print("El resultado de la circunferencia es", r_c)
        
    if Figuras == 3:
        TRAPECIO = C_T = input("Porfavor dime que quieres calcular del Trapecio te puedo hallar: \nArea (a) \nBase Mayor (b) \nBase Menor (bm) \nAltura (h) ")
    
        if C_T == "a" or "Area":
            c_bm1 = float(input("Porfavor necesito que me ingreses el dato de Base Menor (bm) ingreselo en decimal (float): "))
            c_b1 = float(input("Porfavor necesito que me ingreses el dato de Base Mayor (b) ingreselo en decimal (float): "))
            c_h1 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_a3 = ((c_b1 + c_bm1) * c_h1) / 2
            print("El resultado del area es", r_a3)

        elif C_T == "b" or "Base Mayor":
            c_a4 = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            c_bm2 = float(input("Porfavor necesito que me ingreses el dato de Base Menor (bm) ingreselo en decimal (float): "))
            c_h2 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_b2 = ((2 * c_a4) / c_h2) - c_bm2
            print("El resultado de la Base Mayor es", r_b2)

        elif C_T == "bm" or "Base Menor":
            c_a5 = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            c_b2 = float(input("Porfavor necesito que me ingreses el dato de Base Mayor (b) ingreselo en decimal (float): "))
            c_h3 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_bm1 = ((2 * c_a5) / c_h3) - c_b2
            print("El resultado de la Base Menor es", r_bm1)

        elif C_T == "h" or "Altura":
            c_a6 = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            c_b3 = float(input("Porfavor necesito que me ingreses el dato de Base Mayor (b) ingreselo en decimal (float): "))
            c_bm3 = float(input("Porfavor necesito que me ingreses el dato de Base Menor (bm) ingreselo en decimal (float): "))
            r_h2 = (2 * c_a6) / (c_b3 + c_bm3)
            print("El resultado de la Altura es", r_h2)
    if Figuras == 4:
        PARALELOGRAMO = C_P = input("Porfavor dime que quieres calcular del Paralelogramo te puedo hallar: \nArea (a) \nBase (b) \nAltura (h) \nPerimetro (p) ")

        if C_P == "a" or "Area":
            c_b5 = float(input("Porfavor necesito que me ingreses el dato de Base (b) ingreselo en decimal (float): "))
            c_h5 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_a4 = c_b5 * c_h5
            print("El resultado del area es", r_a4)

        elif C_P == "b" or "Base":
            c_a7 = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            c_h6 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_b3 = c_a7 / c_h6
            print("El resultado de la Base es", r_b3)

        elif C_P == "h" or "Altura":
            c_a8 = float(input("Porfavor necesito que me ingreses el dato de Area (a) ingreselo en decimal (float): "))
            c_b6 = float(input("Porfavor necesito que me ingreses el dato de Base (b) ingreselo en decimal (float): "))
            r_h3 = c_a8 / c_b6
            print("El resultado de la Altura es", r_h3)

        elif C_P == "p" or "Perimetro":
            c_b7 = float(input("Porfavor necesito que me ingreses el dato de Base (b) que tiene que ser un numero entero (int): "))
            c_l1 = float(input("Porfavor necesito que me ingreses el dato del Lado (l) que tiene que ser un numero entero (int): "))
            r_p2 = 2 * (c_b7 + c_l1)
            print("El resultado del Perimetro es", r_p2)
    if Figuras == 5:
        PARALELEPIPEDO = C_PP = input("Porfavor dime que quieres calcular del Paralelepipedo te puedo hallar: \nVolumen (v) \nLargo (l) \nAncho (a) \nAltura (h) ")

        if C_PP == "v" or "Volumen":
            c_l2 = float(input("Porfavor necesito que me ingreses el dato de Largo (l) ingreselo en decimal (float): "))
            c_a9 = float(input("Porfavor necesito que me ingreses el dato de Ancho (a) ingreselo en decimal (float): "))
            c_h7 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_v1 = c_l2 * c_a9 * c_h7
            print("El resultado del volumen es", r_v1)

        elif C_PP == "l" or "Largo":
            c_v2 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_a10 = float(input("Porfavor necesito que me ingreses el dato de Ancho (a) ingreselo en decimal (float): "))
            c_h8 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_l1 = c_v2 / (c_a10 * c_h8)
            print("El resultado del Largo es", r_l1)

        elif C_PP == "a" or "Ancho":
            c_v3 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_l3 = float(input("Porfavor necesito que me ingreses el dato de Largo (l) ingreselo en decimal (float): "))
            c_h9 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_a10 = c_v3 / (c_l3 * c_h9)
            print("El resultado del Ancho es", r_a10)

        elif C_PP == "h" or "Altura":
            c_v4 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_l4 = float(input("Porfavor necesito que me ingreses el dato de Largo (l) ingreselo en decimal (float): "))
            c_a11 = float(input("Porfavor necesito que me ingreses el dato de Ancho (a) ingreselo en decimal (float): "))
            r_h4 = c_v4 / (c_l4 * c_a11)
            print("El resultado de la Altura es", r_h4)
    if Figuras == 6:
        PRISMA_RECTANGULAR = C_PR = input("Porfavor dime que quieres calcular del Prisma Rectangular te puedo hallar: \nVolumen (v) \nLargo (l) \nAncho (a) \nAltura (h) ")

        if C_PR == "v" or "Volumen":
            c_l5 = float(input("Porfavor necesito que me ingreses el dato de Largo (l) ingreselo en decimal (float): "))
            c_a12 = float(input("Porfavor necesito que me ingreses el dato de Ancho (a) ingreselo en decimal (float): "))
            c_h10 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_v2 = c_l5 * c_a12 * c_h10
            print("El resultado del volumen es", r_v2)

        elif C_PR == "l" or "Largo":
            c_v5 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_a13 = float(input("Porfavor necesito que me ingreses el dato de Ancho (a) ingreselo en decimal (float): "))
            c_h11 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_l2 = c_v5 / (c_a13 * c_h11)
            print("El resultado del Largo es", r_l2)

        elif C_PR == "a" or "Ancho":
            c_v6 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_l6 = float(input("Porfavor necesito que me ingreses el dato de Largo (l) ingreselo en decimal (float): "))
            c_h12 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_a11 = c_v6 / (c_l6 * c_h12)
            print("El resultado del Ancho es", r_a11)

        elif C_PR == "h" or "Altura":
            c_v7 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_l7 = float(input("Porfavor necesito que me ingreses el dato de Largo (l) ingreselo en decimal (float): "))
            c_a14 = float(input("Porfavor necesito que me ingreses el dato de Ancho (a) ingreselo en decimal (float): "))
            r_h5 = c_v7 / (c_l7 * c_a14)
            print("El resultado de la Altura es", r_h5)
    if Figuras == 7:
        CILINDRO = C_CI = input("Porfavor dime que quieres calcular del Cilindro te puedo hallar: \nVolumen (v) \nRadio (r) \nAltura (h) ")

        if C_CI == "v" or "Volumen":
            c_r3 = float(input("Porfavor necesito que me ingreses el dato de Radio (r) ingreselo en decimal (float): "))
            c_h13 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_v3 = pi * (c_r3 ** 2) * c_h13
            print("El resultado del volumen es", r_v3)

        elif C_CI == "r" or "Radio":
            c_v8 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_h14 = float(input("Porfavor necesito que me ingreses el dato de Altura (h) ingreselo en decimal (float): "))
            r_r3 = ((c_v8 / (pi * c_h14)) ** (1/2))
            print("El resultado del Radio es", r_r3)

        elif C_CI == "h" or "Altura":
            c_v9 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            c_r4 = float(input("Porfavor necesito que me ingreses el dato de Radio (r) ingreselo en decimal (float): "))
            r_h6 = c_v9 / (pi * (c_r4 ** 2))
            print("El resultado de la Altura es", r_h6)
    if Figuras == 8:
        ESFERA = C_E = input("Porfavor dime que quieres calcular de la Esfera te puedo hallar: \nVolumen (v) \nRadio (r) ")

        if C_E == "v" or "Volumen":
            c_r5 = float(input("Porfavor necesito que me ingreses el dato de Radio (r) ingreselo en decimal (float): "))
            r_v4 = (4/3) * pi * (c_r5 ** 3)
            print("El resultado del volumen es", r_v4)

        elif C_E == "r" or "Radio":
            c_v10 = float(input("Porfavor necesito que me ingreses el dato de Volumen (v) ingreselo en decimal (float): "))
            r_r4 = ((3 * c_v10) / (4 * pi)) ** (1/3)
            print("El resultado del Radio es", r_r4)
    if Figuras == 9:
        TRIANGULO_RECTANGULO = T_R = float(input("Porfavor dime que quieres calcular de el Triangulo Rectangulo te puedo hallar: \nHipotenusa (h) \nCateto a (ca) \nCateto b (cb): "))
        if T_R == "h" or "Hipotenusa":
            c_ca = float(input("Porfavor necesito que me ingreses el dato de Cateto a (ca) ingreselo en decimal (float): "))
            c_cb = float(input("Porfavor necesito que me ingreses el dato de cateto b (cb) ingreselo en decimal (float): "))
            r_h7 = ((c_ca ** 2) + (c_cb ** 2)) ** (1/2)
            print("El resultado del Radio es", r_h7)
        elif T_R == "ca" or "Cateto a":
            c_h15 = float(input("Porfavor necesito que me ingreses el dato de la Hipotenusa (h) ingreselo en decimal (float): "))
            c_cb1 = float(input("Porfavor necesito que me ingreses el dato de eL Cateto b (cb) ingreselo en decimal (float): "))
            r_ca = (c_h15 ** 2) - (c_cb1 ** 2) **(1/2)
            print("El resultado del Cateto a es", r_ca)
        elif T_R == "cb" or "Cateto b":
            c_h16 = float(input("Porfavor necesito que me ingreses el dato de la Hipotenusa (h) ingreselo en decimal (float): "))
            c_ca1 = float(input("Porfavor necesito que me ingreses el dato de el Cateto a (ca) ingreselo en decimal (float): "))
            r_cb = (c_h16 ** 2) - (c_ca1 ** 2) **(1/2)
            print("El resultado del Cateto b es", r_cb)
        
        
    
    seguir = input("Quiere calcular otra figura si/no: ")
    print("---------------------------------------------------------------------")    
    print("MUCHAS GRACIAS POR USAR NUESTRA MEJOR MARCA DE CALCULADORAS DEL MUNDO")
    print("---------------------------------------------------------------------")
