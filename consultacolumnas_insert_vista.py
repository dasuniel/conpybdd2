import cx_Oracle

try:
    connection = cx_Oracle.connect(
        user='us',
        password='con',
        dsn='con',
        encoding='UTF-8'
    )
    print("Versión de la base de datos:", connection.version)
    
    cursor = connection.cursor()
    
    # Comprobar si la tabla PYT existe
    cursor.execute("SELECT table_name FROM user_tables")
    tables = cursor.fetchall()
    
    if ('PYT',) not in tables:
        print("La tabla 'PYT' no existe.")
    else:
        # Obtener y mostrar las columnas de la tabla PYT
        cursor.execute("SELECT column_name FROM user_tab_columns WHERE table_name = 'PYT'")
        columns = cursor.fetchall()
        print("Columnas en la tabla PYT:")
        for column in columns:
            print(column[0])

        # Insertar datos en la tabla PYT
        cursor.execute("INSERT INTO PYT (ID, NOMBRE, EDAD) VALUES (9, 'Juan Pérez', 30)")
        cursor.execute("INSERT INTO PYT (ID, NOMBRE, EDAD) VALUES (8, 'María García', 25)")
        cursor.execute("INSERT INTO PYT (ID, NOMBRE, EDAD) VALUES (7, 'Carlos López', 40)")
        
        # Confirmar la transacción
        connection.commit()
        print("Datos insertados exitosamente.")
        
        # Verificar los datos insertados
        cursor.execute("SELECT * FROM PYT")
        rows = cursor.fetchall()  # Aquí se guarda el resultado de la consulta

        # Mostrar los datos
        print("Datos en la tabla PYT:")
        for row in rows:
            print(row)  # Imprimir cada fila

except cx_Oracle.DatabaseError as ex:
    print("Error:", ex)
    
finally:
    if connection:
        connection.close()
    print("Conexión finalizada.")
