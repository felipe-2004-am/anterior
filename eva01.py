"""
Programa: eva01.py
Alumno: Felipe Gregorio Amador Mendoza
Matricula:1723110135
Fecha:29/01/24
"""
class profesores():
   id = None
   nombre = None
   materias = []


   def __init__(self, id, nombre):
     self.id = id
     self.nombre = nombre  
     self.materia=[]
     print("ClaseProfesor")


   def califica(self):
     print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre, self.materias[0]))


   def pasaasistencia(self):
     print(f"El profesor {self.nombre} pasa asistencia")



profesor1 = profesores(111,"Profesor 1")
profesor1.materias.append("Materia 1")
profesor1.materias.append("Materia 2")
profesor1.califica()
profesor1.pasaasistencia()

