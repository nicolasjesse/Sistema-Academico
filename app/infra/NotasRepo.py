from app.infra import DatabaseConnection as db


class NotasRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()
    
    def add_nota(self, nota):
        insert_sql = "INSERT INTO nota (valor, aluno_cod, professor_cod, disciplina, bimestre) VALUES ('%d', '%d', '%d', '%s', '%d')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql %(nota.valor, nota.aluno_cod, nota.professor_cod, nota.disciplina, nota.bimestre))
            return True
        except Exception as error:
            raise Exception(error)