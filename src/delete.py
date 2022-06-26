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
            cursor.execute(f"""DROP TABLE {table[0]};
                            """)

        cursor.execute(""" create table CATEGORY(
                        type varchar(50) Not Null,
                        name varchar(50) unique not null,
                        id varchar(50) unique Not null,
                        parentId varchar(50) null,
                        updateDate date Not null
                        );""")
        cursor.execute(""" create table OFFER(
                        type varchar(50) Not Null,
                        name varchar(50) not null,
                        id varchar(50) unique Not null,
                        parentId varchar(50),
                        price int Not null,
                        updateDate date Not null
                        );""")

except Exception as ex:
    print("[!] ERrOR", ex)
finally:
    if connection:
        connection.close()
