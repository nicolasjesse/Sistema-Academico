from app.models.Grade import Grade


class Boletim:

    def __init__(self, grade):
        self.notas = {}
        for disciplina in grade.disciplinas:
            self.notas[disciplina]={1:{None, None}, 2:{None, None}, 3:{None, None}, 4:{None, None}}
