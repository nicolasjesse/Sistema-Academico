class User:

    def __init__(self, cod, nome, cpf, email, senha, tipo, telefone=None):
        self.cod = cod
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.tipo = tipo

