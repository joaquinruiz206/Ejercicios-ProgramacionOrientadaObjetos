class Materia:
    
    def __init__(self,dni,nombre,fecha,nota,aprobado):
        self.__dni=dni
        self.__nombre=nombre
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobado=aprobado
        
        
    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getFecha(self):
        return self.__fecha

    def getNota(self):
        return self.__nota
    
    def getAprobado(self):
        return self.__aprobado
    
    