import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from app.infra.NotasRepo import NotasRepo


notasrepo = NotasRepo()

class Boletim(tk.Frame):

    def __init__(self, parent, screen, notas, disciplina):
        tk.Frame.__init__(self, parent)
        notas = notas[disciplina]
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
        self.dicd['main'].place(x=self.comecox+2, y=(self.comecoy+2)+self.thisy//3, width=self.thisx//5, height=self.thisy//9)
        self.dicn1 = {}
        self.dicn1['main'] = tk.Label(self.parent, text="BIM 1")
        self.dicn1['main'].place(x=(self.comecox+2)+self.thisx//5, y=(self.comecoy+2)+self.thisy//3, width=self.thisx//5, height=self.thisy//9)
        self.dicn2 = {}
        self.dicn2['main'] = tk.Label(self.parent, text="BIM 2")
        self.dicn2['main'].place(x=(self.comecox+2)+2*self.thisx//5, y=(self.comecoy+2)+self.thisy//3, width=self.thisx//5, height=self.thisy//9)
        self.dicn3 = {}
        self.dicn3['main'] = tk.Label(self.parent, text="BIM 3")
        self.dicn3['main'].place(x=(self.comecox+2)+3*self.thisx//5, y=(self.comecoy+2)+self.thisy//3, width=self.thisx//5, height=self.thisy//9)
        self.dicn4 = {}
        self.dicn4['main'] = tk.Label(self.parent, text="BIM 4")
        self.dicn4['main'].place(x=(self.comecox+2)+4*self.thisx//5, y=(self.comecoy+2)+self.thisy//3, width=self.thisx//5, height=self.thisy//9)

        self.parent.widlistreg.append(self.dicd)
        self.parent.widlistreg.append(self.dicn1)
        self.parent.widlistreg.append(self.dicn2)
        self.parent.widlistreg.append(self.dicn3)
        self.parent.widlistreg.append(self.dicn4)

        self.dicd[disciplina] = tk.Label(self.parent, text=disciplina)
        self.dicd[disciplina].place(x=self.comecox+2, y=(self.comecoy+2)+self.thisy//(5//2), width=self.thisx//5, height=self.thisy//9)
        self.dicn1[disciplina] = tk.Button(self.parent, text=notas[1], borderwidth=0, command=partial(self.show_entry, {'cod':notas['cod1'], 'bim':1, 'disciplina':disciplina}))
        self.dicn1[disciplina].place(x=(self.comecox+2)+self.thisx//5, y=(self.comecoy+2)+self.thisy//(5//2), width=self.thisx//5, height=self.thisy//9)
        self.dicn2[disciplina] = tk.Button(self.parent, text=notas[2], borderwidth=0, command=partial(self.show_entry, {'cod':notas['cod2'], 'bim':2, 'disciplina':disciplina}))
        self.dicn2[disciplina].place(x=(self.comecox+2)+2*self.thisx//5, y=(self.comecoy+2)+self.thisy//(5//2), width=self.thisx//5, height=self.thisy//9)
        self.dicn3[disciplina] = tk.Button(self.parent, text=notas[3], borderwidth=0, command=partial(self.show_entry, {'cod':notas['cod3'], 'bim':3, 'disciplina':disciplina}))
        self.dicn3[disciplina].place(x=(self.comecox+2)+3*self.thisx//5, y=(self.comecoy+2)+self.thisy//(5//2), width=self.thisx//5, height=self.thisy//9)
        self.dicn4[disciplina] = tk.Button(self.parent, text=notas[4], borderwidth=0, command=partial(self.show_entry, {'cod':notas['cod4'], 'bim':4, 'disciplina':disciplina}))
        self.dicn4[disciplina].place(x=(self.comecox+2)+4*self.thisx//5, y=(self.comecoy+2)+self.thisy//(5//2), width=self.thisx//5, height=self.thisy//9)

    def show_entry(self, list):
        self.update()
        self.dic = {}
        self.list = list
        self.parent.widlistreg.append(self.dic)
        if list['bim'] == 1:
            self.dic['botao'] = self.dicn1[list['disciplina']]
        elif list['bim'] == 2:
            self.dic['botao'] = self.dicn2[list['disciplina']]
        elif list['bim'] == 3:
            self.dic['botao'] = self.dicn3[list['disciplina']]
        elif list['bim'] == 4:
            self.dic['botao'] = self.dicn4[list['disciplina']]
        self.dic['entry'] = tk.Entry(self.parent)
        self.dic['entry'].insert(tk.END, self.dic['botao']['text'])
        self.dic['entry'].place(x=self.dic['botao'].winfo_x(), y=self.dic['botao'].winfo_y(), height=self.dic['botao'].winfo_height(), width=self.dic['botao'].winfo_width())
        self.dic['entry'].bind('<Return>', self.concluir)
        
    def concluir(self, event):
        try:
            self.dic['botao']['text'] = self.dic['entry'].get()
            notasrepo.update_nota(self.list['cod'], float(self.dic['entry'].get()))
            messagebox.showinfo("Nota alterada com sucesso!", "Nota alterada com sucesso!")
            self.dic['entry'].destroy()
        except Exception as error:
            raise Exception(error)