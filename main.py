class Alumnos:
  matricula:None
  nombre:None
  def __init__(self, matricula, nombre):
    self.matricula=matricula
    self.nombre = nombre
    print("Objeto Alumnos")
objectAlumnos=Alumnos(111, "Juan")
print(objectAlumnos.nombre)
print(objectAlumnos.matricula )
objectAlumnos=Alumnos(nombre="john", matricula=222)
print(objectAlumnos.nombre)
print(objectAlumnos.matricula)
