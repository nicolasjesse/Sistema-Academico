import tkinter as tk
from app.infra.UserRepo import UserRepo
from app.models.User import User
from tkinter import messagebox


userrepo = UserRepo()

class Register(tk.Frame):

    def __init__(self, parent, screen):
        tk.Frame.__init__(self, parent)

        self.father = screen
        self.parent = parent
        parent.destroy_reg()
        self.comecox = (parent.appw//8)
        self.comecoy = (parent.apph//len(screen.lbuttons_dic))
        self.meiox = ((parent.appw-self.comecox)//2)+self.comecox
        self.meioy =  ((parent.apph-self.comecoy)//2)+self.comecoy

        self.dic = {}
        self.parent.widlistreg.append(self.dic)
        self.dic['alunoButton'] = tk.Button(parent, text="Cadastrar um Aluno", command=self.aluno_cadastro, font="Arial, %s" % str(parent.appw//80))
        self.dic['professorButton'] = tk.Button(parent, text="Cadastrar um Professor", command=self.professor_cadastro, font="Arial, %s" % str(parent.appw//80))

        for button in self.dic:
            self.dic[button].place(x=10000, y=10000)
        
        self.update()

        cont = 0
        for button in self.dic:
            self.dic[button].place(width=parent.appw//4, x=self.meiox-((parent.appw//4)//2), y=((self.meioy+(cont*self.dic[button].winfo_height()))-(self.dic[button].winfo_height()//2))-self.parent.apph//12)
            cont += 1

    def aluno_cadastro(self):
        self.parent.destroy_reg()
        self.dice = {}
        self.dicl = {}
        self.parent.widlistreg.append(self.dice)
        self.parent.widlistreg.append(self.dicl)

        try:
            self.dice['nomeEntry'] = tk.Entry(self.parent)
            self.dice['cpfEntry'] = tk.Entry(self.parent)
            self.dice['emailEntry'] = tk.Entry(self.parent)
            self.dice['senhaEntry'] = tk.Entry(self.parent, show="*")
            self.dice['telefoneEntry'] = tk.Entry(self.parent)
            self.dice['confirmarButton'] = tk.Button(self.parent, text="Confirmar", command=self.confirmar_cadastro_aluno, font="Arial, %s" % str(self.parent.appw//80))

            self.dicl['nomeLabel'] = tk.Label(self.parent, text="Nome:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['cpfLabel'] = tk.Label(self.parent, text="CPF:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['emailLabel'] = tk.Label(self.parent, text="Email:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['senhaLabel'] = tk.Label(self.parent, text="Senha:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['telefoneLabel'] = tk.Label(self.parent, text="Telefone:", font="Arial, %s" % str(self.parent.appw//80))

            for entry in self.dice:
                self.dice[entry].place(x=10000, y=10000)
            for label in self.dicl:
                self.dicl[label].place(x=10000, y=10000)

            self.update()

            cont=0
            for entry in self.dice:
                self.dice[entry].place(x=self.meiox-(self.dice[entry].winfo_width()//2), y=(self.meioy+(cont*self.dice[entry].winfo_height()))-self.parent.apph//6)
                cont += 1

            cont=0
            for label in self.dicl:
                self.dicl[label].place(x=self.meiox-(self.dice['nomeEntry'].winfo_width()), y=(self.meioy+(cont*self.dice['nomeEntry'].winfo_height()))-self.parent.apph//6)
                cont += 1

        except Exception as error:
            raise Exception(error)

    def confirmar_cadastro_aluno(self):
        user = User(0, self.dice['nomeEntry'].get(), self.dice['cpfEntry'].get(), self.dice['emailEntry'].get(), self.dice['senhaEntry'].get(), 'ALUNO', self.dice['telefoneEntry'].get())
        if userrepo.add_user(user):
            self.father.show_register()
            messagebox.showinfo("Concluído", "Usuário cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro!", "Dados ja cadastrados")

    def confirmar_cadastro_professor(self):
        user = User(0, self.dice['nomeEntry'].get(), self.dice['cpfEntry'].get(), self.dice['emailEntry'].get(), self.dice['senhaEntry'].get(), 'PROFESSOR', self.dice['telefoneEntry'].get())
        if userrepo.add_user(user):
            self.father.show_register()
            messagebox.showinfo("Concluído", "Usuário cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro!", "Dados ja cadastrados")

    def professor_cadastro(self):
        self.parent.destroy_reg()
        self.dice = {}
        self.dicl = {}
        self.parent.widlistreg.append(self.dice)
        self.parent.widlistreg.append(self.dicl)

        try:
            self.dice['nomeEntry'] = tk.Entry(self.parent)
            self.dice['cpfEntry'] = tk.Entry(self.parent)
            self.dice['emailEntry'] = tk.Entry(self.parent)
            self.dice['senhaEntry'] = tk.Entry(self.parent, show="*")
            self.dice['telefoneEntry'] = tk.Entry(self.parent)
            self.dice['confirmarButton'] = tk.Button(self.parent, text="Confirmar", command=self.confirmar_cadastro_professor, font="Arial, %s" % str(self.parent.appw//80))

            self.dicl['nomeLabel'] = tk.Label(self.parent, text="Nome:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['cpfLabel'] = tk.Label(self.parent, text="CPF:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['emailLabel'] = tk.Label(self.parent, text="Email:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['senhaLabel'] = tk.Label(self.parent, text="Senha:", font="Arial, %s" % str(self.parent.appw//80))
            self.dicl['telefoneLabel'] = tk.Label(self.parent, text="Telefone:", font="Arial, %s" % str(self.parent.appw//80))

            for entry in self.dice:
                self.dice[entry].place(x=10000, y=10000)
            for label in self.dicl:
                self.dicl[label].place(x=10000, y=10000)

            self.update()
            
            cont=0
            for entry in self.dice:
                self.dice[entry].place(x=self.meiox-(self.dice[entry].winfo_width()//2), y=(self.meioy+(cont*self.dice[entry].winfo_height()))-self.parent.apph//6)
                cont += 1

            cont=0
            for label in self.dicl:
                self.dicl[label].place(x=self.meiox-(self.dice['nomeEntry'].winfo_width()), y=(self.meioy+(cont*self.dice['nomeEntry'].winfo_height()))-self.parent.apph//6)
                cont += 1

        except Exception as error:
            raise Exception(error)
