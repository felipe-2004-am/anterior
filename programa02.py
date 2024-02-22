"""
   Nombre: Felipe Gregorio AM
   Matricula:1723110135
   Grupo: TI21
   Fecha: 18/01/2024
   Descripción: Defenir un metodo que se llama mas tarde
"""
class A:                                  #Define una clase llamada A
  matricula=None                          #Declara  la variable matricula
  nombre=None                             #Declara  la variable nombre
  def __init__(self, matricula, nombre):  #Define el metodo init
     print("Constructor de la clase A")   #Imprime "constructor de la clase A"
  
objectA= A(111,"a")                       #Genera una instancia de la clase A
print(objectA.nombre)                     #Imprime "None"
