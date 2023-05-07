import csv
from Clase import PlanAhorro

def agregar(self,item):
    self.happend(item)

def cargar(self):
    arch=open("datos.csv","r")
    fila=csv.reader(arch,delimiter=';')
    
    for i in fila:
        obj=PlanAhorro(i[0],i[1],i[2],i[3])
        self.agregar(obj)
    
    
    