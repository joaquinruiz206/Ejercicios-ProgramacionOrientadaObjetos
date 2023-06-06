class Ventana:
    def __init__(self,tit:str ,xsup=0,ysup=0,xinf=500,yinf=500):
        if(xsup>=0 and ysup>=0 and xinf<=500 and yinf<=500):
            if(xsup<xinf and ysup<yinf):
                self.__titulo=tit
                self.__xsup=xsup
                self.__ysup=ysup
                self.__xinf=xinf
                self.__yinf=yinf
            else:
                raise ValueError ("El valor ingresado para xsup es mayor a xinf o el ysup es mayor a yinf")
        else:
            raise ValueError ("Se ingreso mal los valores iniciales para crear la ventana, por favor el x e y superior tienen que ser mayor a 0 o igual y los inferiores menor o igual a 500.")
    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__yinf-self.__ysup
    
    def ancho(self):
        return self.__xinf-self.__xsup
    
    def mostrar(self):
        print(f"superiro: ({self.__xsup},{self.__ysup}) inferior: ({self.__xinf},{self.__yinf})")
        print(f"altura:{self.alto()} ancho:{self.ancho()}")
    
    def moverIzquierda(self,cant=0):
        self.__xsup-=cant
        self.__xinf-=cant
        
    def moverDerecha(self,cant=0):
        self.__xsup+=cant
        self.__xinf+=cant
        
    def subir(self,cant=0):
        self.__ysup+=cant
        self.__yinf+=cant
        
    def bajar(self,cant=0):
        self.__ysup-=cant
        self.__yinf-=cant