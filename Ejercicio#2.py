#Resistro de Estuiantes
# Descripcion: Crea una clase Estudiante que represente a un estudiante
# la clase debe tener atributos como nombre, edad, y calificacion.
# implemente un metodo para calcular si el estudiante aprobo o reprobo
# basandose en su calificacion.#

#Creamos la clase estudiante con sus respectivos atributos
class Estudiante():
    def __init__(self, nombre, edad, calificacion):
      self.nombre = nombre
      self.edad = edad
      self.calificacion = calificacion
#definimos el metodo calcular nota el cual nos permite saber el estado del estudiante
    def Calcular_nota(self):
      if(self.calificacion >= 3.0):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota: {self.calificacion}")
        print("El estudiante APROBRO")
      else:
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota: {self.calificacion}")
        print("El estudiante REPROBO")

#Creamos el objeto
estudiante1 = Estudiante("Juan", 25, 3.0)
estudiante2 = Estudiante("Maria", 22,2.9)

estudiante1.Calcular_nota()
estudiante2.Calcular_nota()
        
