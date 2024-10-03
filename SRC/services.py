from conexao import *

def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)


def criar_usuario(nome, email, senha):
    if conn.is_connected():
        print("Conectado com o banco")

        cursor = conn.cursor()

        sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
        val = (nome, email, senha)

        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        cursor.close()
    else:
        print("Não Conectado com o banco")

def listar_usuario():
    if conn.is_connected():
        print("Conectado com o banco")

        cursor = conn.cursor()

        cursor.execute("select id, nome, email from usuario;")

        usuarios = cursor.fetchall()
        return usuarios
    else:
        print("Falha ao conectar com o banco de dados!")