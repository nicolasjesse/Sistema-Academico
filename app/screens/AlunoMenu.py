import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from app.screens.aluno_screens.Inicio import Inicio
from app.screens.aluno_screens.Boletim import Boletim
from functools import partial
from app.infra.NotasRepo import NotasRepo


notasrepo = NotasRepo()

class AlunoMenu(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        lbuttons_width = parent.appw//8
        self.lbuttons_dic = {}
        self.imgGetter = Image.open("app/img/User.png")
        self.imgResizer = self.imgGetter.resize((parent.appw//20, parent.appw//20), Image.ANTIALIAS)
        self.userImg = ImageTk.PhotoImage(self.imgResizer)
        self.lbuttons_dic['imagem'] = tk.Button(image=self.userImg, highlightthickness=0, bd=0, command=self.img_click)
        self.lbuttons_dic['botao1'] = tk.Button(text="Inicio",font="Arial, %s" % str(parent.appw//80), highlightthickness=0, bd=0, command=self.show_inicio)
        self.lbuttons_dic['botao2'] = tk.Button(text="Minhas notas", font="Arial, %s" % str(parent.appw//80), highlightthickness=0, bd=0, command=partial(self.show_notas, notasrepo.get_notas_by_user_cod(self.parent.userSession.cod)))
        self.lbuttons_dic['botao_sair'] = tk.Button(text="Sair", font="Arial, %s" % str(parent.appw//80), highlightthickness=0, bd=0, command=self.voltar)
        cont = 0
        for button in self.lbuttons_dic:
            self.lbuttons_dic[button].place(height=parent.apph//len(self.lbuttons_dic), width=lbuttons_width, x=0, y=cont*parent.apph//len(self.lbuttons_dic))
            cont+=1
        self.border_dic = {}
        cont = 0
        for cont in range(len(self.lbuttons_dic)):
            self.border_dic[cont]=ttk.Separator(orient=tk.HORIZONTAL)
            self.border_dic[cont].place(bordermode=tk.OUTSIDE, height=None, width=lbuttons_width, x=0, y=cont*parent.apph//(len(self.lbuttons_dic)))

        self.nomeLabel = tk.Label(text=parent.userSession.nome+"("+parent.userSession.tipo+")", font="Arial, %s" % str(parent.appw//50))
        self.nomeLabel.place(x=10000, y=10000)
        self.update()
        self.nomeLabel.place(x=(((parent.appw-(parent.appw//8))//2)+(parent.appw//8))-self.nomeLabel.winfo_width()//2, y=((self.parent.apph//len(self.lbuttons_dic))//2)-self.nomeLabel.winfo_height()//2)

        self.separadorHORI = ttk.Separator(orient=tk.HORIZONTAL)
        self.separadorHORI.place(bordermode=tk.OUTSIDE, height=None, width=parent.appw, x=0, y=parent.apph//len(self.lbuttons_dic))
        self.separadorVERT = ttk.Separator(orient=tk.VERTICAL)
        self.separadorVERT.place(bordermode=tk.OUTSIDE, height=parent.apph, width=None, x=parent.appw//8, y=0)

    def img_click(self, event=None):
        print("opa")
    
    def show_inicio(self):
        show_inicio = Inicio(self.parent, self)
        show_inicio.place(x=0, y=0)
    
    def show_notas(self, notas):
        show_boletim = Boletim(self.parent, self, notas)
        show_boletim.place(x=0, y=0)

    def voltar(self):
        self.parent.userSession = None
        self.parent.destroy_screen()
        self.parent.show_login()
