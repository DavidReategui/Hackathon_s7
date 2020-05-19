from pymongo import MongoClient
from conexion.conexion_mdb import Conexion
import atributos_conexion

conexion = Conexion(atributos_conexion.CADENA_DE_CONEXION_MONGODB,atributos_conexion.BASE_DATOS_MONGODB) 

class Alumno:
    
    def __init__(self, codigo = 0, nombre = ''):
        self.nombre = nombre
        self.codigo = codigo
        self.notas = []
        self._promedio = 0

        #---
        self.collection = "Alumno"

    @staticmethod
    def obtener_desde_consola():
        nombre = input("Ingrese el nombre del alumno: ")
        codigo_alumno = input("Ingrese el codigo del alumno: ")
        return Alumno(nombre, codigo_alumno)

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def obtener_promedio(self):
        if len(self.notas) > 0:
            self._promedio = sum(self.notas) // len(self.notas)
        return self._promedio

    def __str__(self):
        nombre = f"Nombre del Alumno: {self.nombre}"
        codigo = f"Codigo del Alumno: {self.codigo_alumno}"
        notas_a_imprimir = ""
        for i, nota in enumerate(self.notas):
            notas_a_imprimir += f"Nota #{i+1} : {nota}\n"
        if len(self.notas) == 0:
            notas_a_imprimir = "El alumno no tiene notas registradas."
        promedio = f"Promedio del Alumno: {self.obtener_promedio()}"
        return "\n".join((nombre, codigo, notas_a_imprimir, promedio))
# --- David
    def nuevo(self):
        documento={'codigo':self.codigo, 'nombre':self.nombre}
        ret_nuevo = conexion.insert(self.collection,documento)
        print(ret_nuevo)
    
    def listar(self):
        cur_data = conexion.mostrar_all(self.collection,'')
        lis_codigos = []
        if len(cur_data) > 0:
            print('____________________________________________________')
            print('* ID ......... Nombres y Apellidos .................')
            print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
            for dato in cur_data:
                print(f"* {dato['codigo']} . {dato['nombre'].ljust(30,' ')} ")
                lis_codigos.append(dato['codigo'])

        else:
            print( 'No Encontro ALUMNOS a listar...')
        
        return lis_codigos

    def eliminar(self, _id):
        cond = {'codigo':_id}
        ret_eliminar = conexion.eliminar_documento(self.collection, cond)
        return ret_eliminar

    def modificar(self ):
        cond = {'codigo':self.codigo}
        sett = {"$set":{'nombre':self.nombre}}
        ret_eliminar = conexion.modificar_documento(self.collection, cond, sett)
        return ret_eliminar


class Docente:
    
    def __init__(self, codigo = 0, nombre = '', especialidad = ''):
        
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad
        #---
        self.collection = "Docente"

    @staticmethod
    def obtener_desde_consola():
        nombre = input('Ingresar el nombre del docente: ')
        codigo = input('Ingresar el codigo del docente: ')
        return Docente(nombre, codigo)

    def __str__(self):
        nombre = f"Nombre del docente: {self.nombre}"
        codigo = f"Codigo del docente: {self.codigo_docente}"
        return "\n".join((nombre, codigo))
    
    def nuevo(self):
        documento={'codigo':self.codigo, 'nombre':self.nombre, 'especialidad':self.especialidad}
        ret_nuevo = conexion.insert(self.collection,documento)
        print(ret_nuevo)
    
    def listar(self):
        cur_data = conexion.mostrar_all(self.collection,'')
        lis_codigos = []
        if len(cur_data) > 0:
            print('____________________________________________________')
            print('* ID ......... Nombres y Apellidos .... Especialidad')
            print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
            for dato in cur_data:
                print(f"* {dato['codigo']} . {dato['nombre'].ljust(30,' ')} . {dato['especialidad']}")
                lis_codigos.append(dato['codigo'])

        else:
            print( 'No Encontro DOCENTES a listar...')
        
        return lis_codigos

    def eliminar(self, _id):
        cond = {'codigo':_id}
        ret_eliminar = conexion.eliminar_documento(self.collection, cond)
        return ret_eliminar

    def modificar(self ):
        cond = {'codigo':self.codigo}
        sett = {"$set":{'nombre':self.nombre}}
        ret_eliminar = conexion.modificar_documento(self.collection, cond, sett)
        return ret_eliminar





