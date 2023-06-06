from ClaseMateria import Materia
import csv

class listaMaterias:
    def __init__(self):
        self.__lista=[]
        
    def carga(self):
        arch=open("materiasAprobadas.csv" "r")
        lectura=csv.reader(arch,delimiter=";")
        
        ban=True
        for dato in lectura:
            if ban:
                ban=False
            else:
                obj=Materia(int(dato[0]), dato[1], dato[2], int(dato[3]), dato[4])
                self.__lista.append(obj)
        arch.close()
        
    def calcProm(self,dni):
        promA=0
        promSA=0
        contA=0
        contSA=0
            
        for materia in self.__lista:
            if materia.getDni() ==dni:
                nota=materia.getNota()
                if nota < 4:
                    promA += nota
                    contA += 1
                else:
                    promA += nota
                    contA += 1
                    
                    promSA += nota
                    contSA += 1
        print(f"Promedio del alumno: {dni}")
        print(f"Con aplazos {promA/contA}")
        print(f"Sin aplazos {promSA/contSA}")
            
        def Datos(self, materia):
            listaMateriaSolicitada = []
            for objeto in self.__lista:
                materia_nombre = objeto.getNombre()
                materia_nota = objeto.getNota()
                if materia_nombre == materia and materia_nota >= 7:
                    listaMateriaSolicitada.append(objeto)
                    return listaMateriaSolicitada