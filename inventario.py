nombre = ""
precio = 0.0
cantidad = 0

#CREACION DE VARIABLES PARA QUE EL CODIGO LAS RECONOZCA

while True:
        print("1.Registrar producto")
        print("2.Salir del menu: ")
        print("3.Mostrar ultimo producto guardado")
        menu = int(input("ingrese el numero del menu : "))

        #SE UTILIZA EL BUCLE WHILE PARA LA CREACION DE UN MENU

        if(0<menu<=3):
                print(f"ingreso al menu con el codigo {menu}")
        else:
            print(f"{menu} no existe en el menu")

        # SE UTILIZA UNA VALIDACION PARA VERIFICAR QUE SE INGRESE 
        # UN NUMERO RECONOCIDO POR EL SISTEMA
        if(menu ==1):
            while(True):
                try:
                    nombre = input("ingrese el nombre del producto: ")
                    break
                except ValueError:
                    print("ingrese el nombre de manera correcta")
            while(True):
                try:
                    precio = float(input("ingrese el precio: "))
                    break
                except ValueError:
                    print("el precio debe ser un numerico")
            while(True):       
                try:
                    cantidad = int(input(f"ingrese la cantidad del producto {nombre}: "))
                    break
                except ValueError:
                    print("la cantidad de ser un numero entero")
            costo_total = (precio*cantidad)

        # SE UTILIZA UNA VALIDACION EN CASO DE QUE EL USUARIO QUIERA
        # REGISTRAR UN PRODUCTO NUEVO
        if(menu == 2):
             print("ADIOSS")
             break
        
        # VALIDACION DE QUE EL USUARIO QUIERE SALIR DEL MENU

        if(menu == 3):
            if(nombre == ""):
                 print("")
                 print("no ha guardado productos")
            else:
                 print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Total: {costo_total}")
            
            # VALIDACION DE QUE EL USUARIO DESEA SABER 
            # SOBRE EL PRODUCTO REGISTRADO 