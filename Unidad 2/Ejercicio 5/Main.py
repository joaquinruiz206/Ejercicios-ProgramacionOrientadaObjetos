
from Lista import Lista

if __name__ == "__main__":
    
    lista=Lista()
    lista.cargar()
    
    
    print("1:Actualizar el valor de vehiculo de todos los planes. \n")
    print("2: Mostrar Info Vehiculo con monto menor a la cuota ingresada \n")
    print("3: Mostrar monto para licitar vehiculo \n")
    print("4: Ingresar codigo de plan para cambiar cuotas para licitar \n")
    print("0: Salir")
    opcion=int(input("Ingresar opcion a realizar"))
    while (opcion >=1 and opcion<=4) : 
        if(opcion==1):
            lista.actualizaValor()
        if(opcion==2):
            lista.mostrarMenorCuota()
        if(opcion==3):
            lista.mostrarMontoLisitar()
        if(opcion==4):
            lista.codigoCambiar()
        print("1:Actualizar el valor de vehiculo de todos los planes. \n")
        print("2: Mostrar Info Vehiculo con monto menor a la cuota ingresada \n")
        print("3: Mostrar monto para licitar vehiculo \n")
        print("4: Ingresar codigo de plan para cambiar cuotas para licitar \n")
        print("0: Salir")
        opcion=int(input("Ingresar opcion a realizar"))