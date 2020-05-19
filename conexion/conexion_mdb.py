from pymongo import MongoClient, errors
from logger import escribir_al_log

class Conexion:
    def __init__(self, uri, database):
        # Ejemplo uri = 'mongodb://localhost:27017') 
        self.client = MongoClient(uri)
        # Ejemplo database = 'sesion_1')
        self.db = self.client[database]
        

    def insert(self, collection, data):
        collection = self.db[collection]
        result = collection.insert_one(data)
        print(f'Insert ID: {result.inserted_id}')
          
    def mostrar_xcondicion(self, collection, _condicion = '*', _campos='*' ):
        collection = self.db[collection]
        result = collection.find(_condicion)

        return list(result)

    def mostrar_all(self, collection, condicion=''):
        #-- SELECT MANY
        documentos = []
        cl = self.db[collection]
        try:
            if condicion == '':
                resultado = cl.find()
            else:
                resultado = cl.find(condicion)

            documentos = list(resultado)
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al buscar los documentos en la BD MongoDB"
            )
        return documentos
    
    def eliminar_documento(self, collection, condicion):
        #-- DELETE
        cl = self.db[collection]
        eliminacion_exitosa = False
        #print('DARH : ',condicion)
        try:
            resultado = cl.delete_one(condicion)
            eliminacion_exitosa = resultado.deleted_count > 0
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al eliminar el documento de la BD MongoDB"
            )
        return eliminacion_exitosa

    def modificar_documento(self, collection, condicion, newvalues):
        #-- DELETE
        cl = self.db[collection]
        eliminacion_exitosa = False
        print('DARH : ',condicion, newvalues)
        try:
            resultado = cl.update_one(condicion, newvalues)
    
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al eliminar el documento de la BD MongoDB"
            )
        
        else: 
            print(f'Actualizado ID: {resultado.upserted_id}')
        

