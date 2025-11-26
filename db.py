import sqlite3

def conectar():
    return sqlite3.connect("myDB.db")

def obtener_personas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM personas")
    datos = cursor.fetchall()
    conexion.close()
    return datos

def insertar_persona(nombre, apellido):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO personas (nombre, apellido) VALUES (?, ?)", (nombre, apellido))
    conexion.commit()
    conexion.close()

def actualizar_persona(id, nombre, apellido):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE personas SET nombre=?, apellido=? WHERE id=?", (nombre, apellido, id))
    conexion.commit()
    conexion.close()

def eliminar_persona(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM personas WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

