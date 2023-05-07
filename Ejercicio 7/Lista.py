import csv
from Clase import Viajero

class Lista:
    __lista = []
    
    def __init__(self):
        self.__lista=[]
    
    def agregar(self,obj):
        self.__lista.append(obj)
        
    def cargaLista(self):
        archivo=open('dato.csv')
        datos= csv.reader(archivo,delimiter=';')
        
        bandera = False
        for fila in datos:
            if(bandera):
                bandera=True
            else:
                obj= Viajero(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.agregar(obj)
                
    def mostrar(self):
        for via in self.__lista :
            via.datos()
            
    