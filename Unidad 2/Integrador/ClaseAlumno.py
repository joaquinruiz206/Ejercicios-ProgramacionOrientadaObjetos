class Alumno: 
    def __init__(self,dni,apellido,nombre,carrera,ano):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__año=ano
        
            
    def getDni(self):
        return self.__dni

    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getCarrera(self):
        return self.__carrera
    
    def getAño(self):
        return self.__año
    
    def __str__(self):
        return f"{self.__año}  {self.__apellido}  {self.__nombre}"

    def __lt__(self, otro):
        if self.__anio == otro.__anio:
            return self.__apellido < otro.__apellido
        else:
            return self.__anio < otro.__anio
