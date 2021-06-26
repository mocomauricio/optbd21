import psycopg2
from datetime import datetime


while(True):
    try:
            connection = psycopg2.connect(user="postgres",
                                          password="postgres",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="tpbd")
            cursor = connection.cursor()


            funcionario_id = input("Leer RFID: ")
            sql_select_query = """select id, nombre, cedula from funcionarios_funcionario where id = %s"""
            cursor.execute(sql_select_query, (funcionario_id,))
            record = cursor.fetchone()

            while(record == None):
                print("ERROR, funcionario no existe...")
                funcionario_id = input("Leer RFID: ")
                sql_select_query = """select * from funcionarios_funcionario where id = %s"""
                cursor.execute(sql_select_query, (funcionario_id,))
                record = cursor.fetchone()

            temperatura = float(input("Ingrese temperatura: ") )
            fecha_hora_actual = datetime.now()

            postgres_insert_query = """ INSERT INTO funcionarios_marcacion (funcionario_id, fecha, hora, temperatura, imagen) VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = ( record[0], 
                                 fecha_hora_actual.date(),
                                 fecha_hora_actual.time(), 
                                 temperatura, 
                                 'fotos/índice.jpg')
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print("Marcacion registrada")


            if(temperatura > 37):
                print("TEMPERATURA MAYOR A 37º, SONAR ALARMA!!!")

    except (Exception, psycopg2.Error) as error:
            print("ERROR: Fallo al insertar datos en la tabla", error)

    finally:
            # closing database connection.
            if connection:
                    cursor.close()
                    connection.close()
                    #print("PostgreSQL connection is closed")