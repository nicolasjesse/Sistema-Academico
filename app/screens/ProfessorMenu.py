import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class ProfessorMenu(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        lbuttons_width = parent.appw//8
        self.lbuttons_dic = {}
        ##IMAGEM
        self.imgGetter = Image.open("app/img/User.png")
        self.imgResizer = self.imgGetter.resize((50, 50), Image.ANTIALIAS)
        self.userImg = ImageTk.PhotoImage(self.imgResizer)
        self.lbuttons_dic['imagem'] = tk.Button(image=self.userImg, highlightthickness=0, bd=0, bg='grey', command=self.img_click)
        ##BOTOES LATERAIS
        self.lbuttons_dic['botao1'] = tk.Button(text="Inicio",font="Arial, 12", highlightthickness=0, bd=0, bg='white')
        self.lbuttons_dic['botao2'] = tk.Button(text="botao1", font="Arial, 12", highlightthickness=0, bd=0, bg='white')
        self.lbuttons_dic['botao3'] = tk.Button(text="botao2", font="Arial, 12", highlightthickness=0, bd=0, bg='white')
        self.lbuttons_dic['botao4'] = tk.Button(text="botao3", font="Arial, 12", highlightthickness=0, bd=0, bg='white')
        self.lbuttons_dic['botao_sair'] = tk.Button(text="Sair", font="Arial, 12", highlightthickness=0, bd=0, command=self.quit, bg='white')
        cont = 0
        for button in self.lbuttons_dic:
            self.lbuttons_dic[button].place(height=parent.apph//len(self.lbuttons_dic), width=lbuttons_width, x=0, y=cont*parent.apph//len(self.lbuttons_dic))
            cont+=1
        ##BORDA
        self.border_dic = {}
        cont = 0
        for cont in range(len(self.lbuttons_dic)):
            self.border_dic[cont]=ttk.Separator(orient=tk.HORIZONTAL)
            self.border_dic[cont].place(bordermode=tk.OUTSIDE, height=None, width=lbuttons_width, x=0, y=cont*parent.apph//(len(self.lbuttons_dic)))

        self.separadorHORI = ttk.Separator(orient=tk.HORIZONTAL)
        self.separadorHORI.place(bordermode=tk.OUTSIDE, height=None, width=parent.appw, x=0, y=parent.apph//len(self.lbuttons_dic))
        self.separadorVERT = ttk.Separator(orient=tk.VERTICAL)
        self.separadorVERT.place(bordermode=tk.OUTSIDE, height=parent.apph, width=None, x=parent.appw//8, y=0)

    def img_click(self, event=None):
        print("opa")