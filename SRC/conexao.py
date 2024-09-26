import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = "carvalho",
    host = "localhost",
    password = "project_crud",
    db = "projeto_crud"
)

if conn.is_connected():
    print("Conectado com o banco")
else:
    print("Não Conectado com o banco")