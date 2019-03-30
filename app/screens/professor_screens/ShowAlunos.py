import tkinter as tk
from app.models.User import User
from app.infra.UserRepo import UserRepo
from app.infra.NotasRepo import NotasRepo
from functools import partial
from app.screens.professor_screens.Boletim import Boletim


notasrepo = NotasRepo()
userrepo = UserRepo()

class ShowAlunos(tk.Frame):

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
        self.lbuttons_dic = screen.lbuttons_dic

        self.dic = {}
        self.dicl = {}
        self.parent.widlistreg.append(self.dic)
        self.parent.widlistreg.append(self.dicl)
        self.alunos = userrepo.get_users_by_type('ALUNO')

        for aluno in self.alunos:
            self.dic[aluno.cod] = tk.Button(self.parent, text=aluno.nome, command=partial(self.show, aluno), borderwidth=0)

        cont = 0
        for button in self.dic:
            self.dic[button].place(x=self.comecox+2, y=(self.comecoy+2)+cont*(self.thisy//len(self.dic)), width=self.thisx, height=self.thisy//len(self.dic))
            cont += 1

    def show(self, aluno):
        self.parent.destroy_reg()
        self.visitedSession = aluno
        self.dicl['boletim'] = tk.Button(self.parent, text="BOLETIM", borderwidth=1, command=partial(self.show_boletim, self.visitedSession.cod))
        self.dicl['matricula'] = tk.Button(self.parent, text="Matrícula: "+str(aluno.cod), borderwidth=0)
        self.dicl['nome'] = tk.Button(self.parent, text="Nome: "+aluno.nome, borderwidth=0, command=partial(self.pushentry, 'nome'))
        self.dicl['cpf'] = tk.Button(self.parent, text="CPF: "+aluno.cpf, borderwidth=0, command=partial(self.pushentry, 'cpf'))
        self.dicl['email'] = tk.Button(self.parent, text="Email: "+aluno.email, borderwidth=0, command=partial(self.pushentry, 'email'))
        self.dicl['senha'] = tk.Button(self.parent, text="Senha: "+aluno.senha, borderwidth=0, command=partial(self.pushentry, 'senha'))
        self.dicl['telefone'] = tk.Button(self.parent, text="Telefone: "+aluno.telefone, borderwidth=0, command=partial(self.pushentry, 'telefone'))
        


        for widget in self.dicl:
            self.dicl[widget].place(x=10000, y=10000)

        self.update()

        cont = 0
        for widget in self.dicl:
            self.dicl[widget].place(x=self.comecox+2, y=(self.comecoy+2)+cont*(self.thisy//len(self.dicl)), height=self.thisy//len(self.dicl), width=self.thisx-2)
            cont += 1
    
    def show_boletim(self, cod):
        pass
        boletim_show = Boletim(self.parent, self, notasrepo.get_notas_by_user_cod(cod))
        boletim_show.place(x=0, y=0)
        
    def pushentry(self, dado):
        self.update()
        self.dado = dado
        self.entry = tk.Entry(self.parent)
        self.some_dic = {}
        self.some_dic[dado]=self.entry
        self.parent.widlistreg.append(self.some_dic)
        self.entry.insert(tk.END, self.dicl[dado]['text'])
        self.entry.place(x=self.dicl[dado].winfo_x(), y=self.dicl[dado].winfo_y(), height=self.thisy//len(self.dicl), width=self.thisx-2)
        self.entry.bind('<Return>', self.concluir)
        return self.entry
    
    def concluir(self, event):
        try:
            self.dicl[self.dado]['text']= self.entry.get()
            self.aluno = self.visitedSession
            user = User(self.aluno.cod, self.dicl['nome']['text'][6:], self.dicl['cpf']['text'][5:], self.dicl['email']['text'][7:], self.dicl['senha']['text'][7:], 'ALUNO', self.dicl['telefone']['text'][10:])
            if userrepo.update_user(user):
                print("yay")
            self.entry.destroy()
        except Exception as error:
            raise Exception(error)