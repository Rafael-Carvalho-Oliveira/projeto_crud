from tkinter import *
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


    janela = Tk()
    janela.geometry("400x400")
    janela.title("Sistema de Gerenciamento de Usuário")

    #Cor de fundo
    janela.configure(background = "#f0f0f0")

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

    listar = Button(janela, text = "Listar Usuários", width = 15, font = ("Comic Sans MS", 10))
    listar.place(x = 250, y = 200)

    janela.mainloop()

if __name__ == "__main__":
    main()