class Usuario:

    # Constructor
    def __init__(self, id, nombre, matricula, carrera, correo, activo = True):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
        self.activo = activo # Por defecto, el usuario esta activo

        def activar(self):
            self.activo = True
            

        def desactivar(self):
            self.activo = False

        def mostrar_info(self):
            return f"Usuario ID: {self.id}, Nombre: {self.nombre}, Matricula: {self.matricula}, Carrera: {self.carrera}, Correo: {self.correo}, Activo: {'Si' if self.activo else 'No'}"