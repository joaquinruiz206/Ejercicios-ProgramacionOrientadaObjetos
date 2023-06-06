class Conjunto: 
    
    def __init__(self,lista):
        self.__lista= []
        for i in lista:
            self.__lista.append(i)
            
    def mostrar(self):
        return self.__lista
    
    def ordena(self):
        return self.__lista.sort()
            
    def __add__(self,obj):
        nuevaList=[]
        for i in self.__lista:
            nuevaList.append(i)
            for j in obj.__lista:
                if j not in self.__lista:
                    nuevaList.append(j)
        return nuevaList
    
    def __sub__(self,obj):
        nuevaList=[]
        for i in self.__lista:
            if i not in obj:
                nuevaList.append(i)
        return nuevaList
        
    def __eq__(self, o):
        bandera=False
        if len(self.__lista)==len(o.__lista):
            for i in self.__lista:
                if i in o:
                    bandera=True
            for j in o:
                if j in self.__lista:
                    bandera=True
        return bandera