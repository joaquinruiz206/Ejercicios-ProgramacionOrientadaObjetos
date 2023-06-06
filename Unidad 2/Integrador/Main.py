
from ListaAlumno import ListaAlumnos
from ListaMateria import listaMaterias

if __name__=="__main__":
    materias=listaMaterias()
    materias.cargar()
    
    alumnos=ListaAlumnos()
    alumnos.cargaLista()
    
    op=input("Ingresar la opcion a realizar")

    while op != 0:
        if op == 1:
            dni = int(input("Ingrese dni de alumno para ver promedio "))
            materias.calculoProm(dni)
        elif op == 2:
            materia = input("Ingrese materia a buscar ")
            
            lista = materias.devolverDatos(materia)
            for obj in lista:
                
                alumno = manejadorA.buscaDatos(obj.getDni())
                print("DNI           Apellido y Nombre            Fecha         Nota             Año que cursa")
                print(f"{alumno.getDni()},    {alumno.getNombre()}, {alumno.getApellido()}              {obj.getFecha()}     {obj.getNota()}              {alumno.getAnioCursa()}")

        elif op == 3:
            print("Listado alumnos ordenado:    ")
            alumnos.ordenar()
            alumnos.muestra()
        else:
        opciones = int(input("Ingrese opcion "))