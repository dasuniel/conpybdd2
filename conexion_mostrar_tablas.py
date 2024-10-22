import cx_Oracle

try:
    connection = cx_Oracle.connect(
        user='us',
        password='con',
        dsn='cone',
        encoding='UTF-8'
    )
    print("Versión de la base de datos:", connection.version)
    
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM user_tables")
    tables = cursor.fetchall()
    
    print("Tablas disponibles para el usuario:")
    for table in tables:
        print(table[0])
        
    if ('PYT',) not in tables:
        print("La tabla 'pyt' no existe.")
        
except cx_Oracle.DatabaseError as ex:
    print("Error:", ex)
    
finally:
    if connection:
        connection.close()
    print("Conexión finalizada.")
