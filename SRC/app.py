from tkinter import *
from tkinter import ttk
import services

def main():
    def on_enviar():
        nome = nomeEntry.get()
        email = emailEntry.get()
        senha = senhaEntry.get()
        services.enviar_dados(nome, email, senha)

        nomeEntry.delete(0, END)
        emailEntry.delete(0, END)
        senhaEntry.delete(0, END)

    def deletar_user(email):
        email = emailEntry.get()
        services.remover_usuario(email)

    def listar_usuario():
        usuarios = services.listar_usuario()

        janela_listar = Toplevel(janela)
        janela_listar.title("Lista de Usuários")
        janela_listar.geometry("600x300")

        #Criar uma Treeview(view, vizualização) da lista de usuários, show = "headings" para limpar o cabeçalho

        tree = ttk.Treeview(janela_listar, columns=("ID", "Nome", "Email"), show = "headings")
        tree.heading("ID", text = "ID")
        tree.heading("Nome", text = "Nome")
        tree.heading("Email", text = "Email")

        #criar um botão de voltar que irá fechar a tela de lista de usuários

        voltar = Button(janela_listar, text = "Voltar", font = ("Comic Sans MS", 20), command = janela_listar.destroy)
        voltar.pack(fill = BOTH, expand = True, side = BOTTOM)

        tree.pack(fill = BOTH, expand = True)

        #Inserir os dados dos usuários na Treeview

        for usuario in usuarios:
            #END vai inserir o item no final da tabela
            tree.insert("", END, values = usuario)



    janela = Tk()
    janela.geometry("400x400")
    janela.title("Sistema de Gerenciamento de Usuário")


    #Titulo
    titulo = Label(janela, text = "Crud", font = ("Comic Sans MS", 20))
    titulo.pack(pady = 30)

    #Nome
    nome = Label(janela, text = "Nome: ", font = ("Comic Sans MS", 10))
    nome.place(x = 40, y = 100)

    global nomeEntry
    nomeEntry = Entry(janela, width = 30, text = "Nome: ")
    nomeEntry.place(x = 100, y = 100)

    #Email
    email = Label(janela, text = "Email: ", font = ("Comic Sans MS", 10))
    email.place(x = 40, y = 130)

    global emailEntry
    emailEntry = Entry(janela, width = 30, text = "Email: ")
    emailEntry.place(x = 100, y = 130)

    #Senha
    senha = Label(janela, text = "Senha: ", font = ("Comic Sans MS", 10))
    senha.place(x = 40, y = 160)

    global senhaEntry
    senhaEntry = Entry(janela, text = "Senha: ", width = 30, show = "*")
    senhaEntry.place(x = 100, y = 160)

    cadastrar = Button(janela, text = "Cadastrar", width = 15, font = ("Comic Sans MS", 10), command = on_enviar)
    cadastrar.place(x = 100, y = 200)

    listar = Button(janela, text = "Listar Usuários", width = 15, font = ("Comic Sans MS", 10), command = listar_usuario)
    listar.place(x = 250, y = 200)

    remover = Button(janela, text = "Remover Usuário", width = 15, font = ("Comic Sans MS", 10), command = lambda: deletar_user(email))
    remover.place(x = 100, y = 240)

    janela.mainloop()

if __name__ == "__main__":
    main()