import tkinter as tk
from app.models.User import User
from app.infra.UserRepo import UserRepo
from functools import partial


userrepo = UserRepo()

class ShowProfessores(tk.Frame):

    def __init__(self, parent, screen):
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
        
        self.dic = {}
        self.dicl = {}
        self.parent.widlistreg.append(self.dic)
        self.parent.widlistreg.append(self.dicl)
        self.professores = userrepo.get_users_by_type('PROFESSOR')

        for professor in self.professores:
            self.dic[professor.cod] = tk.Button(self.parent, text=professor.nome, command=partial(self.show, professor), borderwidth=0)

        cont = 0
        for button in self.dic:
            self.dic[button].place(x=self.comecox+2, y=(self.comecoy+2)+cont*(self.thisy//len(self.dic)), width=self.thisx, height=self.thisy//len(self.dic))
            cont += 1

    def show(self, professor):
        self.parent.destroy_reg()
        self.visitedSession = professor
        self.dicl['matricula'] = tk.Button(self.parent, text="Matrícula: "+str(professor.cod), borderwidth=0)
        self.dicl['nome'] = tk.Button(self.parent, text="Nome: "+professor.nome, borderwidth=0, command=partial(self.pushentry, 'nome'))
        self.dicl['cpf'] = tk.Button(self.parent, text="CPF: "+professor.cpf, borderwidth=0, command=partial(self.pushentry, 'cpf'))
        self.dicl['email'] = tk.Button(self.parent, text="Email: "+professor.email, borderwidth=0, command=partial(self.pushentry, 'email'))
        self.dicl['senha'] = tk.Button(self.parent, text="Senha: "+professor.senha, borderwidth=0, command=partial(self.pushentry, 'senha'))
        self.dicl['telefone'] = tk.Button(self.parent, text="Telefone: "+professor.telefone, borderwidth=0, command=partial(self.pushentry, 'telefone'))
        


        for widget in self.dicl:
            self.dicl[widget].place(x=10000, y=10000)

        self.update()

        cont = 0
        for widget in self.dicl:
            self.dicl[widget].place(x=self.comecox+2, y=(self.comecoy+2)+cont*(self.thisy//len(self.dicl)), height=self.thisy//len(self.dicl), width=self.thisx-2)
            cont += 1
            
        
    def pushentry(self, dado):
        self.update()
        self.dado = dado
        self.entry = tk.Entry(self.parent)
        self.entry.insert(tk.END, self.dicl[dado]['text'])
        self.entry.place(x=self.dicl[dado].winfo_x(), y=self.dicl[dado].winfo_y(), height=self.thisy//len(self.dicl), width=self.thisx-2)
        self.entry.bind('<Return>', self.concluir)
        return self.entry
    
    def concluir(self, event):
        try:
            self.dicl[self.dado]['text']= self.entry.get()
            self.professor = self.visitedSession
            user = User(self.professor.cod, self.dicl['nome']['text'][6:], self.dicl['cpf']['text'][5:], self.dicl['email']['text'][7:], self.dicl['senha']['text'][7:], 'PROFESSOR', self.dicl['telefone']['text'][10:])
            userrepo.update_user(user)
            self.entry.destroy()
        except Exception as error:
            raise Exception(error)