import csv
from Clase import PlanAhorro

class Lista:
    def __init__(self):
        self.__lista=[]
        
    def agregar(self,item):
        self.__lista.append(item)
        
    def cargar(self):
        arch=open("datos.csv","r")
        fila=csv.reader(arch,delimiter=';')
            
        for i in fila:
            obj=PlanAhorro(int(i[0]),i[1],i[2],int(i[3]))
            self.__lista.append(obj)
            print(obj)

    def actualizaValor(self):
        for i in self.__lista:
            print("Valor anterior es: ",i.getValor())
            i.setValor(input("Ingresar nuevo valor"))
            print(f"El nuevo valor del vehiculo es: {i.getValor()}")
            
    def mostrarMenorCuota(self):
        valor=int(input("Ingresar valor del vehiculo para buscar"))
        for i in self.__lista:
            if(float(i.valorCouta()) <valor):
                print(i)
                
    def mostrarMontoLisitar(self):
        for i in self.__lista:
            print(f"Monto a pagar: {i.montoLicitar()}")
            
    def codigoCambiar(self):
        cod=int(input("Ingresar el codigo a cambiar las coutas a licitar: "))
        i=0
        while(self.__lista[i].getCodigo()!=cod and i<len(self.__lista)):
            i+=1
            
        if(i<len(self.__lista)):
            print("Se encontro el codigo del vehiculo a buscar, ingresar el cambio de coutas: ")
            self.__lista[i].setCoutasPagas(input(""))
        else:
            print("No se encontro el vehiculo!")