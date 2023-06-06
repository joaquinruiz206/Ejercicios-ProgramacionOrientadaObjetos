from Clase import Conjunto

if __name__ == "__main__":
    lista1=[1,2,3,4]
    lista2=[4,2,1,3]
    
    conj1=Conjunto(lista1)
    conj2=Conjunto(lista2)
    
    print(f"Conjunto 1: {conj1.ordena}")
    print(f"Conjunto 2: {conj2.ordena}")
    
    print("Ingresar 1 si desea unir conjuntos. \n")
    print("Ingresar 2 si desea restar los conjuntos. \n")
    print("Ingresar 3 si desea comparar los conjuntos. \n")
    print("Ingresar 0 si desea finalizar. \n")
    opcion=input("Ingresar valor: ")
    while opcion!=0:
        
        if opcion==1:
            conj3=conj1+conj2
            print(f"La union de los dos conjuntos es: {conj3}")
        if opcion==2:
            conj3=conj1-conj2
            print(f"La resta de los conjuntos 1 y 2 es: {conj3}")
        if opcion==3:
            if conj1 == conj2:
                print("Los conjuntos son iguales. ")
            else:
                print("Los conjuntos son distintos. ")
        
        print("Ingresar 1 si desea unir conjuntos. \n")
        print("Ingresar 2 si desea restar los conjuntos. \n")
        print("Ingresar 3 si desea comparar los conjuntos. \n")
        print("Ingresar 0 si desea finalizar. \n") 
        opcion=input("Ingresar valor")