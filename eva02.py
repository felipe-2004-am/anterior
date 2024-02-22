"""
Programa: eva02.py
Nombre completo (nombre primer_apellido segundo_apellido):Felipe_Gregorio_Amador_Mendoza
Matricula:1723110135
Fecha:29/01/24
"""
class Libro():
   titulo = None
   autor = None
   prestado = None
   anio_publicacion = None
   genero = None
  
   def __init__(self, titulo, autor, anio_publicacion, genero, prestado=False):
    self.titulo = titulo
    self.autor = autor
    self.anio_publicacion = anio_publicacion
    self.genero = genero
    self.prestado = prestado
  

   def prestar(self):
    self.prestado = True


   def devolver(self):
    self.prestado = False


   def mostrar_informacion(self):
       print(f"Titulo: {self.titulo}\n")
       print(f"Autor: {self.autor}")
       print(f"Año de publicación: {self.anio_publicacion}")
       print(f"Género: {self.genero}")
       print(f"Prestado: {'Sí' if self.prestado else 'No'}")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción",True)
libro1.prestar()
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro1.devolver()
libro1.mostrar_informacion()
libro2.mostrar_informacion()
