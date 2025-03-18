#Creamos la clase y sus atributos
class libro():
    def __init__(self,titulo,autor,npaginas):
        self.titulo = titulo
        self.autor = autor
        self.npaginas = npaginas
        pass

#Definimos el metodo Que mostrar los atributos en la salida del codigo
    def MostrarLibro(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Paginas: {self.npaginas}")

#Definimos el metodo para actualizar o modificar el numero de paginas que tendra el libro mediante un condicional
    def ActualizarLibro(self,opcion):
        opcion = int(input("Desea actualizar el numero de paginas? \n"
                "SI:1 / NO:2\n"
                "Opcion: "))
        if (opcion == 1):
            pagina = int(input("Digite nuevo numero de paginas para el libro: "))
            print(f"El numero de paginas se actualizo a {pagina}")
            self.npaginas = pagina
            print(f"Titulo: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Paginas: {self.npaginas}")
        else:
            print(f"Titulo: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Paginas: {self.npaginas}")

#instaciamos el objeto    
libro1 = libro("El principito", "Antonie", 120)

libro1.MostrarLibro()
libro1.ActualizarLibro("30")