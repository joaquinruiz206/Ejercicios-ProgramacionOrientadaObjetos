from ManejaSabores import ManejaSabores
from ManejaHelados import ManejaHelados



if __name__ == "__main__":
    
    manejaSabores = ManejaSabores()
    manejaSabores.cargar()
    manejaHelados = ManejaHelados()
    
    
    print("1: Registrar un Helado Vendido.")
    print("2: Mostrar el nombre de los 5 Helados mas vendidos.")
    print("3: Ingresar el ID del sabor y informar los gramos mas vendidos.")
    print("4: Ingresar tipo de helado en gramos y mostrar los sabores mas vendidos en ese tamaño.")
    print("5: Total recaudado.")
    op = int(input("Ingrese opcion: "))
    while op <6:
        if op == 1:
            cantidad = 0
            sabores = []
            manejaSabores.muestra()
            idSabor = int(input("Ingrese sabor de helado, 0 para salir "))
            manejaSabores.contarSabor(idSabor)
            while idSabor != 0 and (cantidad < 3):
                sabor = manejaSabores.busca(idSabor)
                sabores.append(sabor)
                cantidad += 1
                
                
                
                
                idSabor = int(input("Ingrese sabor de helado, 0 para salir "))
                manejaSabores.contarSabor(idSabor)
            
            gramos = int(input("Ingrese cantidad de gramos "))
            precio = int(input("Ingrese precio "))
            
            manejaHelados.addHelado(gramos, precio, sabores)
            
            manejaHelados.muestraHelados()
            
        elif op == 2:
            manejaSabores.ordena()
            manejaSabores.muestraContador()
        elif op == 3:
            manejaSabores.muestra()
            codigo = int(input("Ingrese sabor de helado a buscar: "))
            print(f"Cantidad de gramos del helado solicitado son: {manejaHelados.cuentaGramos(codigo)}")
        elif op == 4:
            tipo = int (input("Ingrese tipo de helado: "))
            print(f"Cantidad de helados de {tipo} gramos, son: {manejaHelados.cuentaTipo(tipo)}")
        elif op == 5:
            print(f"Total vendido: {manejaHelados.sumador()}")
            
        print("1: Registrar un Helado Vendido.")
        print("2: Mostrar el nombre de los 5 Helados mas vendidos.")
        print("3: Ingresar el ID del sabor y informar los gramos mas vendidos.")
        print("4: Ingresar tipo de helado en gramos y mostrar los sabores mas vendidos en ese tamaño.")
        print("5: Total recaudado.")
        op = int(input("Ingrese opcion: "))