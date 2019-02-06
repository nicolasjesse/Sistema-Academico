import tkinter as tk
from app.infra.UserRepo import UserRepo
from tkinter import messagebox


userrepo = UserRepo()


class Login(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.msg = tk.Label(text="Sistema Escolar", font= "Arial, %s" % str(parent.appw//50))
        self.loginLabel = tk.Label(text="Matricula:", font= "Arial, %s" % str(parent.apph//50))
        self.senhaLabel = tk.Label(text="Senha:", font= "Arial, %s" % str(parent.apph//50))
        self.loginEntry = tk.Entry()
        self.senhaEntry = tk.Entry(show="*")
        self.loginButton = tk.Button(text="Entrar", font="Arial, %s" % str(parent.appw//90), command=self.entrar)

        for widget in self.parent.winfo_children():
            widget.place(x=10000, y=10000)
        self.update()

        self.msg.place(x=(self.parent.appw//2)-(self.msg.winfo_width()//2), y=0)
        self.loginLabel.place(x=(self.parent.appw//2)-2*(self.loginLabel.winfo_width()), y=self.parent.apph//2, height=self.parent.apph//20)
        self.update()
        self.senhaLabel.place(x=(self.parent.appw//2)-2*(self.loginLabel.winfo_width()), y=(self.parent.apph//2)+self.loginLabel.winfo_height(), height=self.parent.apph//20)
        self.loginEntry.place(x=(self.parent.appw//2)-(self.loginLabel.winfo_width()), y=self.parent.apph//2, width=self.parent.appw//6, height=self.loginLabel.winfo_height())
        self.senhaEntry.place(x=(self.parent.appw//2)-(self.loginLabel.winfo_width()), y=(self.parent.apph//2)+self.loginLabel.winfo_height(), width=self.parent.appw//6, height=self.loginLabel.winfo_height())
        self.update()
        self.loginButton.place(x=((self.parent.appw//2)-(self.loginLabel.winfo_width()))+self.loginEntry.winfo_width(), y=self.parent.apph//2, height=self.loginEntry.winfo_height()+self.senhaEntry.winfo_height())

    def entrar(self):
        users_list = userrepo.get_users()
        matricula = self.loginEntry.get()
        senha = self.senhaEntry.get()
        for user in users_list:
            if str(user.cod)==matricula and user.senha==senha:
                self.parent.userSession = user    
                self.parent.destroy_screen()
                if user.tipo == 'ADMIN':
                    return self.parent.show_adminmenu()
                elif user.tipo == 'ALUNO':
                    return self.parent.show_alunomenu()
                elif user.tipo == 'PROFESSOR':
                    return self.parent.show_professormenu()
                else:
                    pass
        messagebox.showerror("Erro", "Os dados não constam!")
    
                
                
        