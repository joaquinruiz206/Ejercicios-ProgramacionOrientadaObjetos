class Email:

    
    def __init__(self,idCuenta:str|None,dominio:str|None,tipoDominio:str|None,contraseña:str|None):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__tipoDominio=tipoDominio
        self.__contraseña=contraseña
    
    def getIdCuenta(self):
        return self.__idCuenta
    
    def getDominio(self):
        return self.__dominio
    
    def getTipoDominio(self):
        return self.__tipoDominio
    
    def getConstraseña(self):
        return self.__contraseña
    
    def setContraseña(self,contra):
        self.__contraseña=contra

    def retornaEmail(self):
        return (self.__idCuenta+'@'+self.__dominio+'.'+self.__tipoDominio)
    
    def crearCuenta(self,correo):
        nombre=correo.split('@')
        self.__idCuenta=nombre[0]
        
        dom=correo.split('.')
        self.__dominio=dom[0]
        
        self.__tipoDominio=dom[1]
        
        contra=input("Ingresar contraseña: ")
        
        self.__contraseña=contra
        
        return Email(self.__idCuenta,self.__dominio,self.__tipoDominio, self.__contraseña)

    
    def modificaContraseña(self):
        si=int(input("Desea modificar la contraseña 1=si 0=no: "))
    
        if(si==1):
            contra=input("Ingresar contraseña: ")
            if(contra==self.__contraseña):
                self.setContraseña(input("Ingresar nueva contraseña: "))
            else:
             print("Contraseña incorrecta!")
    