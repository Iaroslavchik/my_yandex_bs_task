import psycopg2
from config import host, password, port, user, db_name
def create_table(json):
    try:
        global connection
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=db_name

        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            for i in json["items"]:
                atribut = ''
                value = ''
                path = i['type']
                for j in i:
                    atribut += str(j) + ', '
                    if isinstance(i[j], str):
                        value += "'" + str(i[j]) + "'" + ', '
                    else:
                        value += str(i[j]) + ', '
                atribut += 'updateDate'
                value += "'" + str(json["updateDate"]) + "'"
                cursor.execute(f'insert into {path}({atribut}) values ({value});')
            print("Table created")

    except Exception as ex:
        print("[ПУПУПУ] EROOR", ex)
    finally:
        if connection:
            connection.close()

