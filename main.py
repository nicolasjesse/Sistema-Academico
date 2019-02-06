import tkinter as tk
from app.screens.Login import Login
from app.screens.AlunoMenu import AlunoMenu
from app.screens.ProfessorMenu import ProfessorMenu
from app.screens.AdminMenu import AdminMenu
from app.models.User import User
from app.infra.UserRepo import UserRepo
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.pcw = self.winfo_screenwidth()
        self.pch = self.winfo_screenheight()
        self.appw = self.pcw*2//3
        self.apph = self.pch*2//3
        self.maxsize(self.appw, self.apph)
        self.minsize(self.appw, self.apph)
        self.x = (self.pcw//2) - (self.appw//2)
        self.y = (self.pch//2) - (self.apph//2)
        self.geometry('%dx%d+%d+%d' % (self.appw, self.apph, self.x, self.y))
        self.title('TEOESCOLAR')
        self.frameSession = None
        self.userSession = None
        self.widlistreg = []
        self.widlist = self.winfo_children()
        self.show_login()
    

    def show_login(self):
        self.login = Login(self)
        self.login.place(x=0, y=0)
        self.frameSession = self.login

    def show_adminmenu(self):
        self.admin_screen = AdminMenu(self)
        self.admin_screen.place(x=0, y=0)
    
    def show_professormenu(self):
        self.professor_screen = ProfessorMenu(self)
        self.professor_screen.place(x=0, y=0)

    def show_alunomenu(self):
        self.aluno_screen = AlunoMenu(self)
        self.aluno_screen.place(x=0, y=0)

    def destroy_screen(self): #reseta a tela apagando todos os widgets
        self.widlist = self.winfo_children()
        for widget in self.widlist:
            widget.destroy()
    
    def destroy_reg(self): #apaga os widgets da mini-tela
        for dic in self.widlistreg:
            for widget in dic:
                dic[widget].destroy()
    
    
app = App()
app.mainloop()