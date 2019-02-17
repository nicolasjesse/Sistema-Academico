import tkinter as tk
from tkinter import ttk


class Boletim(tk.Frame):

    def __init__(self, parent, screen, notas):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.father = screen
        self.parent.destroy_reg()
        self.comecox = (parent.appw//8)
        self.comecoy = (parent.apph//len(screen.lbuttons_dic))
        self.meiox = ((parent.appw-self.comecox)//2)+self.comecox
        self.meioy =  ((parent.apph-self.comecoy)//2)+self.comecoy
        self.thisx = self.parent.appw-self.comecox
        self.thisy = self.parent.apph-self.comecoy
        
        self.dicd = {}
        self.dicd['main'] = tk.Label(self.parent, text="DISCIPLINA")
        self.dicn1 = {}
        self.dicn1['main'] = tk.Label(self.parent, text="BIM 1")
        self.dicn2 = {}
        self.dicn2['main'] = tk.Label(self.parent, text="BIM 2")
        self.dicn3 = {}
        self.dicn3['main'] = tk.Label(self.parent, text="BIM 3")
        self.dicn4 = {}
        self.dicn4['main'] = tk.Label(self.parent, text="BIM 4")

        self.parent.widlistreg.append(self.dicd)
        self.parent.widlistreg.append(self.dicn1)
        self.parent.widlistreg.append(self.dicn2)
        self.parent.widlistreg.append(self.dicn3)
        self.parent.widlistreg.append(self.dicn4)

        for disciplina in notas:
            self.dicd[disciplina] = tk.Label(self.parent, text=disciplina)
        cont = 0
        for label in self.dicd:
            self.dicd[label].place(x=self.comecox+2, y=(self.comecoy+2)+cont*self.thisy//9, width=self.thisx//5, height=self.thisy//9)
            cont += 1
        
        for disciplina in notas:
            self.dicn1[disciplina] = tk.Button(self.parent, text=notas[disciplina][1], borderwidth=0)
        cont = 0
        for label in self.dicn1:
            self.dicn1[label].place(x=(self.comecox+2)+self.thisx//5, y=(self.comecoy+2)+cont*self.thisy//9, width=self.thisx//5, height=self.thisy//9)
            cont += 1

        for disciplina in notas:
            self.dicn2[disciplina] = tk.Button(self.parent, text=notas[disciplina][2], borderwidth=0)
        cont = 0
        for label in self.dicn2:
            self.dicn2[label].place(x=(self.comecox+2)+2*self.thisx//5, y=(self.comecoy+2)+cont*self.thisy//9, width=self.thisx//5, height=self.thisy//9)
            cont += 1

        for disciplina in notas:
            self.dicn3[disciplina] = tk.Button(self.parent, text=notas[disciplina][3], borderwidth=0)
        cont = 0
        for label in self.dicn3:
            self.dicn3[label].place(x=(self.comecox+2)+3*self.thisx//5, y=(self.comecoy+2)+cont*self.thisy//9, width=self.thisx//5, height=self.thisy//9)
            cont += 1
        
        for disciplina in notas:
            self.dicn4[disciplina] = tk.Button(self.parent, text=notas[disciplina][4], borderwidth=0)
        cont = 0
        for label in self.dicd:
            self.dicn4[label].place(x=(self.comecox+2)+4*self.thisx//5, y=(self.comecoy+2)+cont*self.thisy//9, width=self.thisx//5, height=self.thisy//9)
            cont += 1

        self.separadores = {}
        self.parent.widlistreg.append(self.separadores)
        for sep in range(1, len(notas)+1):
            self.separadores[sep] = ttk.Separator(orient=tk.HORIZONTAL)
            self.separadores[sep].place(y=self.comecoy+((self.thisy//9)*sep)+1, bordermode=tk.OUTSIDE, height=None, width=self.thisx, x=self.comecox+2)
        
        for sep in range(1, 6):
            self.separadores['vert'+str(sep)] = ttk.Separator(orient=tk.VERTICAL)
            self.separadores['vert'+str(sep)].place(y=self.comecoy+2, bordermode=tk.OUTSIDE, height=self.thisy, width=None, x=(self.comecox)+((self.thisx//5)*sep)+1)