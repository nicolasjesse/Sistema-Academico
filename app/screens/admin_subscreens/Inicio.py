import tkinter as tk


class Inicio(tk.Frame):
    
    def __init__(self, parent, screen):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.father = screen
        self.comecox = (parent.appw//8)
        self.comecoy = (parent.apph//len(screen.lbuttons_dic))
        self.meiox = ((parent.appw-self.comecox)//2)+self.comecox
        self.meioy =  ((parent.apph-self.comecoy)//2)+self.comecoy
        self.thisx = self.parent.appw-self.comecox
        self.thisy = self.parent.apph-self.comecoy

        self.user = self.parent.userSession
        self.parent.destroy_reg()
        self.dic = {}
        self.parent.widlistreg.append(self.dic)
    
        self.dic['matriculaLabel'] = tk.Label(self.parent, text="Matrícula: "+str(self.user.cod))
        self.dic['cpfLabel'] = tk.Label(self.parent, text="CPF: "+self.user.cpf)
        self.dic['emailLabel'] = tk.Label(self.parent, text="Email: "+self.user.email)
        self.dic['telefoneLabel'] = tk.Label(self.parent, text="Telefone: "+self.user.telefone)


        for label in self.dic:
            self.dic[label].place(x=10000, y=10000)

        self.update()

        cont = 0
        for label in self.dic:
            self.dic[label].place(x=self.comecox+2, y=(self.comecoy+2)+cont*self.thisy//len(self.dic), height=self.thisy//len(self.dic), width=self.thisx)
            cont += 1