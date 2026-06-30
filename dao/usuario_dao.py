#DAO: Data Access Object
#libro_dao: Objeto de acceso a datos de la tabla libro

from database import conexion
from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO:

    #SELECT * from usuario
    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM vista_usuarios" )
        registros = cursor.fetchall()

        usuarios = []
        for reg in registros:
            usuario = Usuario(
                id=reg[0],
                nombre=reg[1],
                matricula=reg[2],
                carrera=reg[3],
                correo=reg[4])
            usuarios.append(usuario)
        cursor.close()
        conexion.close()
        return usuarios
    
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql="""
        INSERT INTO usuario (id, nombre, matricula, carrera, correo)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql,
                       (usuario.id,
                        usuario.nombre,
                        usuario.matricula,
                        usuario.carrera,
                        usuario.correo))
        
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql="""
        UPDATE usuario
        SET nombre = %s,
        matricula = %s, 
        carrera = %s, 
        correo = %s
        WHERE id= %s
        """
        cursor.execute(sql,
                        (usuario.nombre,
                         usuario.matricula,
                         usuario.carrera,
                         usuario.correo,
                         usuario.id))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, usuario_id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM usuario WHERE id = %s", 
            (usuario_id,)
            )
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id FROM usuario ORDER BY id DESC")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado is None:
            return 0
        return resultado[0]