import csv
from ClaseAlumno import Alumno
import numpy as np

class ListaAlumnos:
    def __init__(self):
        self.__arreglo= np.array([], dtype=Alumno)
        
    def cargaLista(self):
        arch=open("alumnos.csv","r")
        datos=csv.reader(arch,delimiter=";")
        
        bandera=True
        
        for fila in datos:
            if bandera:
                bandera=False
            else:
                alu=Alumno(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
                self.__arreglo =np.append(self.__arreglo,alu)
        arch.close()
        
        
    def muestra(self):
        for i in self.__arreglo:
            print(i)
        
    def ordena(self):
        self.__arreglo.sort()
        
                