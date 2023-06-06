class Viajero:
    
    def __init__(self,numero:int,dni:str,nombre:str ,apellido:str ,millas:int ):
        self.__numeroViajero=numero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millasAcumuladas=millas
     
   
    def getNumeroViajero(self):
        return self.__numeroViajero
    
    
   
    def cantidadTotaldeMillas(self):
        return self.__millasAcumuladas
    
    def acumularMillas(self,millas):
        self.__millasAcumuladas+=millas
        return self.__millasAcumuladas
    
    def canjearMillas(self,millas):
        if(self.verificarMillas(millas)):
            self.__millasAcumuladas-=millas                
        else: 
            print(f"la cantidad de millas a canjear es insuficiente, usted posee {self.__millasAcumuladas}")
        return self.__millasAcumuladas
    
    def verificarMillas(self,millas):
        b=False
        if(self.__millasAcumuladas>=millas):
            b==True
        return b
    
    def datos(self):
        return print( (f"{self.__numeroViajero},{self.__nombre},{self.__apellido},{self.__apellido},{self.__millasAcumuladas}"))
    
    
    
    #Sobrecarga Operadores Por Derecha
    #1
    def __eq__(self,obj2):
        bandera=True
        if(self.__millasAcumuladas<obj2.__millasAcumuladas):
            bandera=False
        return bandera
    
    def __req__(self,obj):
        self.__eq__(obj)
    #2
    
    def __add__(self,cant):
        return Viajero(self.__numero, self.__dni, self.__nombre, self.__apellido, self.acumularMillas(cant))
    
    def __radd__(self,cant):
        self.__add__(cant)
    #3
    
    def __sub__(self,cant):
        if(cant<self.__millasAcumuladas):
            return Viajero(self.__numero, self.__dni, self.__nombre, self.__apellido, self.acumularMillas(-cant))
    
    def __rsub__(self, cant):
        if(cant>self.__millasAcumuladas):
            return Viajero(self.__numero, self.__dni, self.__nombre, self.__apellido, self.acumularMillas(-cant))
    
    
    
    
    