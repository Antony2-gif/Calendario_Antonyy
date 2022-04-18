#Importamos la libreia de sqlite3
import sqlite3
from sqlite3 import Error

def Crear_Conexion():
    #Lo creamos en un try para eviar errores y el cierre del programa
    try:
        conn = sqlite3.connect('DB/Calendar.db')
        return conn
    except Error as e:
        print("Error de la conexion " + e)


#Metodo para insertar los datos
def Insertar_Fecha(data):
    #Creamos la conexio
    conn = Crear_Conexion()
    #Creamos el query
    sql =  """INSERT INTO CALENDAR (Fecha,Hora,Horario,Descripcion)
            VALUES(?,?,?,?)"""
    try:
        #Creamos un cursor para hacer las operaciones
        cur = conn.cursor()
        #Ejecutamos el query
        cur.execute(sql,data)
        conn.commit()
        #lastrowid genera el id automatico 
        print("Fecha insertada Correctarmente")
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar " + e)
        return False
    #Cerramos las conexion
    finally:
        if conn:
            cur.close()
            conn.close()
#Metodo para actualizar Fecha
def Actualizar_Fecha(_id,data):
    #Creamos la conexio
    conn = Crear_Conexion()
    #Creamos el query
    sql =  f"""UPDATE CALENDAR SET Fecha = ?,Hora=?,Horario=?,Descripcion=?
            WHERE Id_Calendario = {_id}"""
    try:
        #Creamos un cursor para hacer las operaciones
        cur = conn.cursor()
        #Ejecutamos el query
        cur.execute(sql,data)
        conn.commit()
        #lastrowid genera el id automatico 
        print("Fecha Modificada Correctarmente")
        return True
    except Error as e:
        print("Error al Modificar " + e)
        return False
    #Cerramos las conexion
    finally:
        if conn:
            cur.close()
            conn.close()
#Metodo para elimnar
def Eliminar_Evento(_id):
    conn = Crear_Conexion()
    sql = f"DELETE FROM CALENDAR WHERE Id_Calendario = {_id}"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Evento Eliminado")
        return True
    except Error as e:
        print("Error al elimar :" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


#Sleccinamos todos los datos de la base de datos
def Seleccion_Fechas():
    #Creamos la conexio
    conn = Crear_Conexion()
    #Creamos el query
    sql = "SELECT * FROM Calendar"
    try:
        #Creamos un cursor para hacer las operaciones
        cur = conn.cursor()
        #Ejecutamos el query
        cur.execute(sql)
        calendar = cur.fetchall()
        return calendar
    except Error as e:
        print("Error al seleccinar " + e)
    #Cerramos las conexion
    finally:
        if conn:
            cur.close()
            conn.close()


def Seleccionar_Id(_id):
    conn = Crear_Conexion()
    sql = f"SELECT * FROM Calendar WHERE Id_Calendario = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        fecha = cur.fetchone()
        print("Datos seleccionados")
        return fecha
    except Error as e:
        print("Error al seleccionar " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()