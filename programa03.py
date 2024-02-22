"""
   Nombre: Felipe Gregorio AM
   Matricula:1723110135
   Grupo: TI21
   Fecha: 18/01/2024
   Descripción: 
"""
class Alumnos:                          #Define una clase de nombre Alumnos
  matricula=None                        #Declara una variable de nombre matricula
  nombre=None                           #Declara una variable de nombre nombre
  def __init__(self, matricula, nombre):  #Define el metodo init
    self.matricula=matricula              #Asigna un valor a matricula
    self.nombre=nombre                    #Asigna un valor a nombre
    print("Objeto Alumnos")               #Imprime "Objeto Alumnos"
objectA=Alumnos(1,"q")                       #Crea un objeto de la clase Alumnos