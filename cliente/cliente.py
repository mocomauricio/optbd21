import psycopg2
import os
from datetime import datetime
from picamera import PiCamera
from time import sleep



try:
    while(True):

            connection = psycopg2.connect(user="pi",
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

            nombre_archivo = "foto_" + fecha_hora_actual.strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'


            #print(nombre_archivo)
            #camera = PiCamera()
            #camera.start_preview()
            #sleep(5) # este sleep es necesario porque esto le da tiempo al sensor de la cám$
            #camera.capture('/home/pi/Desktop/optbd21/proyectobd/media/fotos/'+nombre_archivo)
            #camera.stop_preview()
            os.system('raspistill -o  /home/pi/Desktop/optbd21/proyectobd/media/fotos/'+nombre_archivo)



            postgres_insert_query = """ INSERT INTO funcionarios_marcacion (funcionario_id, fecha, hora, temperatura, imagen) VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = ( record[0], 
                                 fecha_hora_actual.date(),
                                 fecha_hora_actual.time(), 
                                 temperatura, 
                                 'fotos/' + nombre_archivo)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print("Marcacion registrada")


            if(temperatura > 37):
                os.system("mplayer /home/pi/Desktop/optbd21/proyectobd/media/alarma.mp3")
                print("TEMPERATURA MAYOR A 37º, SONAR ALARMA!!!")

            cursor.close()
            connection.close()

except (Exception, psycopg2.Error) as error:
    print("ERROR: Fallo al insertar datos en la tabla", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        #print("PostgreSQL connection is closed")
        