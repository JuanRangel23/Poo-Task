#Ejecicio 3
# En una tienda, se necesitan gestionar el inventario de productos de manera eficiente
# para ello, crea una clase Producto con los atributos nombre (nombre de producto)
# precio (precio unitario), y stock (cantidad disponible).
# la clase debe incluir los metodos verificar_disponibilidad(cantidad) que verifique
# si hay suficiente stock para vender la cantidad solicitada
# Vender(cantidad), que reduce el stock si hay disponibilidad o que muestre un mensaje de falta de stock
# y restablecer(cantidad), que aumente el stock del producto. Crea un objeto Producto con los valores
# iniciales: nombre: Laptop, precio:1200 y stock 10, y realize las siguiente operaciones
# verifique si hay 5 unidades disponibles, vender 3 unidades, verificar si hay 8 unidades disponibles
# intentar vender 8 unidades (debe fallar), reabastecer con 10 unidades, adicionales, verificar nuevamente
# si hay 8 unidades. Este ejercicio permite practicar clases, metodos, conficionales y manipulacion
# de datos en un sistem de inventario basico#

#Creamos la clase Producto y sus atributos
class Producto():
    def __init__(self, nombre_producto, precio_unitario, cantidad_disponible):
        self.nombre_producto = nombre_producto
        self.precio_unitario = precio_unitario
        self.cantidad_disponible = cantidad_disponible

#Definimos le metodo que nos permitira saber cuantos unidades tenemos en stock referente a la cantidad solicitada por el usuarios

    def Verificar_diponiblidad(self, cantidad):
        if(self.cantidad_disponible > cantidad):
            print("SI hay Stock para Vender")
            print(f"Unidades disponible: {self.cantidad_disponible}")
        else:
            print("NO hay Stock SUFICIENTE para vender")
#El metodo vender resta las unidades en stock respecto a la cantidad solicitada y la cantidad supera al stock que lance un mensaje al usuario   
    def Vender(self, cantidad):
        if(self.cantidad_disponible > cantidad):
           self.cantidad_disponible -= cantidad
        else:
            print("Stock INSUFICIENTE")
#El metodo restablecer, rellena el stock para que nunca se encuentre vacio
    def Restablecer(self, cantidad):
        self.cantidad_disponible += cantidad
        print(f"Se agregaron {cantidad} unidades de {self.nombre_producto} al stock, STOCK actual {self.cantidad_disponible}")

producto1 = Producto("Laptop",1200, 10)
producto2 = Producto("Laptop",1200, 10)

producto1.Verificar_diponiblidad(5)
producto1.Vender(3)
producto1.Restablecer(10)

producto2.Verificar_diponiblidad(8)
producto2.Vender(8)
producto2.Restablecer(10)
producto2.Verificar_diponiblidad(8)