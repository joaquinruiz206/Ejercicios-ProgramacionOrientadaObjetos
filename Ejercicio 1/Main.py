from Clase import Email

if __name__ == '__main__':
    print("Creando una cuenta:")
    
   # objeto=Email(input("Ingresar id:"),input("Ingresar dominio:"),input("Ingresar Tipo dominio: "),input("Ingresar contraseña:"))
    
    #print("La contrseña es: ",objeto.getConstraseña())
    
    nombre= input("Ingresar nombre: ")
    mail= input("Ingresar email: ")
    
    objeto2= Email(None,None,None,None)
    
    objeto2.crearCuenta(mail)
    
    print(f"Estimado {nombre} te enviaremos tus mensajes a la direccion {mail}")
    
    objeto2.modificaContraseña()
    
 
    
    
    
    