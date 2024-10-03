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
        cursor.close()
        conn.close()
        return usuarios
    else:
        print("Falha ao conectar com o banco de dados")

def remover_usuario(email):
    if conn.is_connected():
        print("Conectado com o banco")

        cursor = conn.cursor()

        sql_select = "select id, nome, email from usuario where email = %s;"
        cursor.execute(sql_select,(email,))
        
        usuario = cursor.fetchone()
        if usuario:
            print("Usuário encontrado")
            sql_delete = "delete from usuario where email = %s;"
            cursor.execute(sql_delete, (email,))
            print(f"Usuário {usuario[1]} deletado com sucesso")
            conn.commit()
            cursor.close()
            conn.close()

        else:
            print("Usuário não encontrado")