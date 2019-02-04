from app.models.User import User
from app.models.Boletim import Boletim


class Aluno(User):

    def __init__(self, cod, nome, cpf, email, senha, tipo, telefone, grade):
        User.__init__(self, cod, nome, cpf, email, senha, tipo, telefone)
        self.boletim = Boletim(grade).notas