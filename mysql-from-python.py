import os
import pymysql

username = os.getenv('USER')

connection =pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        sql = 'select * from Artist'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally: 
    #Close the connection to sql
    connection.close()
