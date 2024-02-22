"""
   Nombre: Felipe Gregorio AM
   Matricula:1723110135
   Grupo: TI21
   Fecha: 18/01/2024
   Descripción: Agrega 2 objetos dandoles valor
"""
class Alumnos:                                        #crea la clase Alumnos
    matricula:None                                      #crea la variable matricula
    nombre:None                                         #crea la variable nombre
    def __init__(self, matricula, nombre):              #define el metodo
        self.matricula=matricula                        #asigna el valor de matricula
        self.nombre = nombre                            #asigna el valor de nombre
        print("Objeto Alumnos")                         #imprime el mensaje objeto Alumno
objectAlumnos=Alumnos(111, "Juan")                      #crea el objeto Alumnos
print(objectAlumnos.nombre)                             #imprime Objeto Alumno y el nombre del objeto Alumnos
print(objectAlumnos.matricula )     #imprime Objeto Alumno y la matricula del objeto Alumnos
objectAlumnos=Alumnos(nombre="john", matricula=222)     #crea el objeto Alumnos
print(objectAlumnos.nombre)                             #imprime Objeto Alumno y el nombre del objeto Alumnos
print(objectAlumnos.matricula)                          #imprime Objeto Alumno y la matricula del objeto Alumnos
