
from Clase import Viajero
from Lista import Lista
import csv

if __name__ == '__main__':
    lista=Lista()
    archivo= open("dato.csv")
    datos= csv.reader(archivo,delimiter=';')
        
    bandera = False
    for fila in datos:
        if(bandera):
            bandera=True
        else:
            obj= Viajero(fila[0],fila[1],fila[2],fila[3],fila[4])
            lista.agregar(obj)
    
    
    lista.mostrar()
    
    