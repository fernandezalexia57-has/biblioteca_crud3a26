class Libro:
    #Constructor de la clase libro
    def __init__(self, id, titulo, autor, isbn, disponible):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    #Método para prestar el libro
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    #Método para devolver el libro
    def devolver(self):
        self.disponible = True

    def mostar_info(self):
        return f"Libro ID {self.id}, Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {'Si' if self.disponible else 'No'}"