import psycopg2
from config import host, password, port, user, db_name
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=db_name

    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("""SELECT table_name FROM information_schema.tables
                    WHERE table_schema = 'public'""")
        for table in cursor.fetchall():
            print(table[0])


except Exception as ex:
    print("[!] ERrOR", ex)
finally:
    if connection:
        connection.close()
