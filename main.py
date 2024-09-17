import sqlite3

conn = sqlite3.connect('farmacia.db')
cursor = conn.cursor()

def crear_tablas():
    cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
    cedula INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS transaccion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monto REAL NOT NULL,
    fecha TEXT NOT NULL,
    metodo_pago TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS medicinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    receta TEXT NOT NULL,
    dosis REAL NOT NULL)''')

    conn.commit()

def crear_cliente(cedula, nombre, edad):
    cursor.execute('INSERT INTO cliente (cedula, nombre, edad) VALUES (?,?,?)', (cedula, nombre, edad))
    conn.commit()

def leer_clientes():
    cursor.execute('SELECT * FROM cliente')
    return cursor.fetchall()

def leer_nombre_clientes():
    cursor.execute('SELECT * FROM cliente')
    resultado = cursor.fetchall()
    for c in resultado:
        print(c[1])

def actualizar_cliente(cedula, nombre, edad):
    cursor.execute('UPDATE cliente SET nombre = ?, edad = ? WHERE cedula = ?', (nombre, edad, cedula))

def eliminar_cliente(cedula):
    cursor.execute('DELETE FROM cliente WHERE cedula = ?', (cedula,))

if __name__ == '__main__':
    crear_tablas()

    print("Creacion de nuevos clientes...")
    crear_cliente(8888231,'Juan Perez', 30)
    crear_cliente(8765321,'Mariana Rodriguez', 31)
    #try:
    #    c = int(input("Cedula: "))
    #    n = input("Nombre: ")
    #    e = int(input("Edad"))
    #except:
    #    print("ERR::Datos invalidos")
    #crear_cliente(c, n, e)

    print("Clientes luego de insercion...")
    print(leer_clientes())

    print("Nombre de clientes...")
    leer_nombre_clientes()

    print("Actualizar cliente...")
    actualizar_cliente(8888231, "Juana Perez", 31)

    print("Clientes luego del cambio...")
    print(leer_clientes())

    print("Eliminacion de clientes...")
    eliminar_cliente(8765321)

    print("Clientes luego de eliminacion...")
    print(leer_clientes())

    conn.close()