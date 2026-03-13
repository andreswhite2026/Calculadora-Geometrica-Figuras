import time
print("Cargando...")
time.sleep(3)   #Esperar 3 segundos
pi = 3.14159265359
print("--------------------------------------------")
print("BIENVENIDO A LA MEJOR CALCULADORA GEOMETRICA")
print("-----CREADA POR EL MEJOR SER HUMANO, YO-----")
print("--------------------------------------------")

seguir = "si"

while seguir == "si":
    Figuras = int(input("Por favor digame en que figura lo puedo ayudar tenemos: \nFIGURAS 2D \n\n1.RECTANGULO \n2.CIRCULO \n3.TRAPECIO \n4.PARALELOGRAMO \n\nFIGURAS 3D \n\n5.PARALELEPIPEDO \n6.PRISMA RECTANGULAR \n7.CILINDRO \n8.ESFERA \n\n9.TRIANGULO RECTANGULO: \n\n"))
    
    if Figuras == 1:
        RECTANGULO = C_R = input("Porfavor dime que quieres calcular del Rectangulo te puedo hallar: \nArea (a) \nBase (b) \nAltura (h) \nPerimetro (p) ")
        if C_R == "a":
            c_b1 = int(input("Porfavor necesito que me ingreses el dato de Base como numero entero (int) (b): "))
            c_h1 = int(input("Porfavor necesito que me ingreses el dato de Altura como numero entero (int) (h): "))
            r_a1 = (c_b1 * c_h1)  
            print("El resultado del area es", r_a1)
        elif C_R == "b":
            c_a2 = int(input("Porfavor necesito que me ingreses el dato de Area (a): "))
            c_h2 = int(input("Porfavor necesito que me ingreses el dato de Altura (h): "))
            r_b1 = (c_a2 / c_h2)
            print("El resultado de la base es", r_b1)
        elif C_R == "h":
            c_a3 = int(input("Porfavor necesito que me ingreses el dato de Area (a): "))
            c_b3 = int(input("Porfavor necesito que me ingreses el dato de Base (b): "))
            r_h1 = (c_a3 / c_b3)
            print("El resultado de la Altura es",r_h1)
        elif C_R == "p":
            c_b4 = int(input("Porfavor necesito que me ingreses el dato de Base (b): "))
            c_h4 = int(input("Porfavor necesito que me ingreses el dato de Altura (h): "))
            r_p1 = (c_b4 + c_h4) * 2
            print("El resultado del perimetro es",r_p1)
    
    if Figuras == 2:
        CIRCULO = C_C = input("Porfavor dime que quieres calcular del Circulo te puedo hallar: \nArea (a) \nRadio (r) \nCircunferencia (c): ")
        if C_C == "a":
            c_r = int(input("Porfavor necesito que me ingreses el dato de Radio (r): "))
            r_a2 = (c_r ** 2) * pi 
            print("El resultado del area es",r_a2)
        elif C_C == "r":
            h_a = int(input("Porfavor necesito que me ingreses el dato de Area (a): "))
            r_r2 = (h_a / pi)**(1/2)
            print("El resultado del radio es",r_r2)

      










    seguir = input("Quiere calcular otra figura si/no: ")
print("---------------------------------------------------------------------")    
print("MUCHAS GRACIAS POR USAR NUESTRA MEJOR MARCA DE CALCULADORAS DEL MUNDO")
print("---------------------------------------------------------------------")