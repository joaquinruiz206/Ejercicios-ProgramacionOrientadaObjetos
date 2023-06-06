from clase_manejaEmpleados import ListaEmpleados



from datetime import datetime

if __name__ == "__main__":
    
    cantidad = int(input("Ingrese cantidad de empleados a registrar: "))

    manejaEmpleados = ListaEmpleados(cantidad)   

    manejaEmpleados.carga()
 
    print("1: Registrar Horas. Ingresando DNI")
    print("2: Monto Total a pagar dada una Tarea que no haya sido finalizada.")
    print("3: Ayuda Economica de sueldos inferior a 150000, mostrar info.")
    print("4: Calcular sueldo de todos los empleados")
    print("0:Salir")

    
    op = int(input("Ingrese la opcion: "))
    
    while op != 0:
        if op == 1:
            dni = input("Ingrese dni de empleado: ")
            horas = int(input("Ingrese cantidad de horas a ingresar: "))
            empleado = manejaEmpleados.buscaDNI(dni)
            if empleado != -1:
                manejaEmpleados.cargaHoras(horas, empleado)
            else:
                print("No se encontró el empleado")
        elif op == 2:
            tarea = input("Ingrese tarea a buscar: ")
            año = input("Ingrese año actual: ")
            mes = input("Ingrese mes actual: ")
            dia = input("Ingrese dia actual: ")
            
            fecha = datetime(int(año), int(mes), int(dia))
            
            empleado = manejaEmpleados.buscaTarea(tarea, fecha)
            
            if empleado != -1:
                if empleado.getFechaFin() > fecha:
                    print("Costo total de la obra: " + str(empleado.getCosto()))
                else:
                    print("La tarea solicitada ya finalizo")                    
            else:
                print("No se encontro la tarea solicitada")
        elif op == 3:
            print("Les corresponde ayuda a: ")
            manejaEmpleados.ayudaEconomica()
        elif op == 4:
            manejaEmpleados.Muestra()
        else:
            print("Ingreso opcion incorrecta")
        
         
        print("1: Registrar Horas. Ingresando DNI")
        print("2: Monto Total a pagar dada una Tarea que no haya sido finalizada.")
        print("3: Ayuda Economica de sueldos inferior a 150000, mostrar info.")
        print("4: Calcular sueldo de todos los empleados")
        print("0:Salir")
        op = int(input("Ingrese la opcion: "))
        