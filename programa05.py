"""
   Nombre: Felipe Gregorio AM
   Matricula:1723110135
   Grupo: TI21
   Fecha: 18/01/2024
   Descripción: Programa que crea objetos, clases y suma
"""
class Alumnos:                                #Crea la clase Alumnos
    matricula:None                            #Crea la variable matricula
    nombre:None                               #Crea la variable nombre
    def __init__(self, matricula, nombre):    #Crea el constructor
        self.matricula = matricula            #Asigna el valor de matricula
        self.nombre = nombre                  #Asigna el valor de nombre
        print("Objeto Alumno")                #Imprime objetos Alumno
    def estudiar(self):                       #define el metodo estudiar
        print(f"{self.nombre} estudia")       #string
    def sumar(self, numero1, numero2):        #define el metodo sumar
        suma=numero1+numero2                  #suma los dos numeros
        print(f"{numero1}+{numero2}={suma}")  #imprime los numeros de la suma y el resultado
dejah=Alumnos("111", "Dejah")                 #crea el objeto dejah
dejah.estudiar()                              #llama al metodo estudiar
dejah.sumar(10,5)                             #llama al metodo sumar
