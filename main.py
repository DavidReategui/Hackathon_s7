import os
# Cree un sistema para hacer el registro de notas de alumnos
from modelos import Docente, Alumno
from app import Aplicacion

def lee_texto(_glosa):
    while True:
        entrada = input(_glosa+' : ')
        try:
            entrada.isalpha()
            return entrada
        except ValueError:
            print("Ingrese solo Texto")

def lee_entero(_glosa):
    while True:
        entrada = input(_glosa+' : ')
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")

def valida_opciones(_selected, _opciones):
    if _selected in _opciones:
        return True
    else:
        return False

def repinta(_O1):
    os.system('cls')
    if _O1 == 1:
        sub_titulo = 'DOCENTES'
    elif _O1 == 2:
        sub_titulo = 'ALUMNOS'
    elif _O1 == 3:
        sub_titulo = 'SALONES'
    elif _O1 == 4:
        sub_titulo = 'CURSOS'
    elif _O1 == 5:
        sub_titulo = 'NOTAS'
    elif _O1 == 6:
        sub_titulo = 'AÑO'
    else:
        sub_titulo = 'SALIR'

    #print('0-------------------2-------------------4-------------------6-------------------8')
    print('+-------------------------------------------------------------------------------+')
    print('+         COLEGIO PRIVADO " JAVIER PERREZ DE CUELLAR "                          +')
    print('+-------------------------------------------------------------------------------+')
    print('+ [1]-Docentes | [2]-Alumnos | [3]-Salones | [4]-Cursos | [5]- Notas | [6]-Año--+')
    print('+-------------------------------------------------------------------------------+')
    if _O1 in (1,2,3,4,5,6):
        print('+ [ %s ] | [1]-Lista | [2]-Nuevo | [3]-Elimina | [4]-Modifica | [0]-MENU +' % sub_titulo.ljust(10,'*'))
        print('+-------------------------------------------------------------------------------+')

def espera_tecla(_glosa = 'Pulse una tecla para continuar'):
    tecla = input(_glosa+'...')

def listado_inicial(_opcion):
    if _O1 == 1:
        sub_titulo = 'DOCENTE'
    elif _O1 == 2:
        sub_titulo = 'ALUMNOS'
    elif _O1 == 3:
        sub_titulo = 'SALONES'
    elif _O1 == 4:
        sub_titulo = 'CURSOS'
    elif _O1 == 5:
        sub_titulo = 'NOTAS'
    elif _O1 == 6:
        sub_titulo = 'AÑO'
    else:
        sub_titulo = 'SALIR'

def ejecuta_opcion(_op, _subop):

    if _op == 1:
        if _subop == 1:
            Odocente = Docente()
            lis_cod_docentes = Odocente.listar()
            espera_tecla()
        if _subop == 2:
            #-- Nuevo Docente
            print('------------------------')
            print(' DOCENTES --> Insercion ')
            print('------------------------')
            codigo = lee_entero('--> Codigo')
            nombre = lee_texto('--> Apellidos y Nombres')
            especialidad = lee_texto('--> Especialidad')
            Odocente = Docente(codigo, nombre, especialidad)
            Odocente.nuevo()
            espera_tecla()
        if _subop == 3 : 
            Odocente = Docente()
            lis_cod_docentes = Odocente.listar()
            id = lee_entero('Ingrese Codigo de docente a eliminar')
            if valida_opciones(id, lis_cod_docentes):
                Odocente.eliminar(id)
                espera_tecla()
            else:
                espera_tecla('Codigo Inexistente')
        if _subop == 4 :
            Odocente = Docente()
            lis_cod_docentes = Odocente.listar()
            id = lee_entero('Ingrese Codigo de docente a Modificar')
            if valida_opciones(id, lis_cod_docentes):
                nombre = lee_texto('Nuevo nombre')
                especialidad = lee_texto('Nueva Especialidad')
                siono = lee_texto('Confirme la MODIFICACION [S/N]')
                if siono.upper() == 'S' : 
                    Odocente = Docente(id, nombre, especialidad)
                    Odocente.modificar()
                    espera_tecla()
            else:
                espera_tecla('Codigo Inexistente')

    if _op == 2:
        # ------- OPCIONES DE ALUMNOS
        if _subop == 1:
            #--- ALUMNO - Listar
            Oalumno = Alumno()
            lis_cod_alumnos = Oalumno.listar()
            espera_tecla()
        if _subop == 2:
            #-- #--- ALUMNO - Nuevo
            print('------------------------')
            print(' ALUMNOS --> Insercion ')
            print('------------------------')
            codigo = lee_entero('--> Codigo')
            nombre = lee_texto('--> Apellidos y Nombres')
            
            Oalumno = Alumno(codigo, nombre)
            Oalumno.nuevo()
            espera_tecla()
        if _subop == 3 : 
            #--- ALUMNO - Eliminar
            Oalumno = Alumno()
            lis_cod_alumnos = Oalumno.listar()
            id = lee_entero('Ingrese Codigo de alumno a eliminar')
            if valida_opciones(id, lis_cod_alumnos):
                Oalumno.eliminar(id)
                espera_tecla()
            else:
                espera_tecla('Codigo Inexistente')
        if _subop == 4 :
            #--- ALUMNO - Modificar
            Oalumno = Alumno()
            lis_cod_alumnos = Oalumno.listar()
            id = lee_entero('Ingrese Codigo de alumno a Modificar')
            if valida_opciones(id, lis_cod_alumnos):
                nombre = lee_texto('Nuevo nombre')
                
                siono = lee_texto('Confirme la MODIFICACION [S/N]')
                if siono.upper() == 'S' : 
                    Oalumno = Alumno(id, nombre)
                    Oalumno.modificar()
                    espera_tecla()
            else:
                espera_tecla('Codigo Inexistente')

    if _op == 3:
        if _subop == 1:
            Odocente = Docente()
            lis_cod_docentes = Odocente.listar()
            espera_tecla()
        if _subop == 2:
            #-- Nuevo Docente
            print('------------------------')
            print(' DOCENTES --> Insercion ')
            print('------------------------')
            codigo = lee_entero('--> Codigo')
            nombre = lee_texto('--> Apellidos y Nombres')
            especialidad = lee_texto('--> Especialidad')
            Odocente = Docente(codigo, nombre, especialidad)
            Odocente.nuevo()
            espera_tecla()
        if _subop == 3 : 
            Odocente = Docente()
            lis_cod_docentes = Odocente.listar()
            id = lee_entero('Ingrese Codigo de docente a eliminar')
            if valida_opciones(id, lis_cod_docentes):
                Odocente.eliminar(id)
                espera_tecla()
            else:
                espera_tecla('Codigo Inexistente')
        if _subop == 4 :
            Odocente = Docente()
            lis_cod_docentes = Odocente.listar()
            id = lee_entero('Ingrese Codigo de docente a Modificar')
            if valida_opciones(id, lis_cod_docentes):
                nombre = lee_texto('Nuevo nombre')
                especialidad = lee_texto('Nueva Especialidad')
                siono = lee_texto('Confirme la MODIFICACION [S/N]')
                if siono.upper() == 'S' : 
                    Odocente = Docente(id, nombre, especialidad)
                    Odocente.modificar()
                    espera_tecla()
            else:
                espera_tecla('Codigo Inexistente')

def main():
    
    flg_01=True
    while flg_01:
        repinta(0)
        opcion = lee_entero('Ingrese la opcion')
        if valida_opciones(opcion, range(6)) : 

            if opcion == 0:
                flg_01 = False
            else : 
                # --- INGRESO de Sub Opcion

                flg_02 = True
                while flg_02 :
                    repinta(opcion)
                    sub_opcion = lee_entero('Que Operacion Requiere')
                    if valida_opciones(sub_opcion, range(5)) : 
                        if sub_opcion == 0:
                            flg_02 = False
                        else:
                            ejecuta_opcion(opcion, sub_opcion)








    if opcion == '1':
        docente_1 = app_registro.registrar_docente()
        print(docente_1)
    elif opcion == '2':
        alumno_1 = app_registro.registrar_alumno()
        print(alumno_1)
    elif opcion == '3':
        alumno_1 = app_registro.buscar_alumno()
        alumno_1 = app_registro.registrar_nota_alumno(alumno_1)
        print(alumno_1)

if __name__ == "__main__":
    main()
