class PlanAhorro:
    __cantCuotas=1
    __cantCuotasPagas=1
   
    
    def __init__(self,codigo:int,modelo:str,version:str,valor:int):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
        
    def getCodigo(self):
        return self.__codigo
    
    def setValor(self,valor):
        self.__valor=valor
        
    def montoLicitar(self):
        return self.__cantCuotasPagas*self.valorCouta()
        
    def valorCouta(self):
        return ((self.getValor() / self.__cantCuotas)+(self.getValor()*0.10))
    
    def getValor(self):
        return self.__valor
    @classmethod
    def setCoutas(cls,cant):
        cls.__cantCuotas=cant
        
    @classmethod
    def setCoutasPagas(cls,cant):
        cls.__cantCuotasPagas=cant
    
    def __str__(self):
        return str(self.__codigo)+";"+self.__modelo+";"+self.__version+";"+str(self.__valor)
    