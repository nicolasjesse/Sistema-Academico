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

    def update_nota(self, nota):
        update_sql = "UPDATE nota SET valor = '%d' WHERE nota_cod = '%d'"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(update_sql % (nota.valor, nota.cod))
            return True
        except Exception:
            return False

    def get_notas_by_user_cod(self, user_cod):
        get_sql = "SELECT valor, bimestre, disciplina FROM nota WHERE aluno_cod='%i'"
        notas = {}
        disciplinas = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql % user_cod)
            results = cursor.fetchall()
            for result in results:
                if result[2] not in disciplinas:
                    disciplinas.append(result[2])
            for disciplina in disciplinas:
                notas[disciplina]={1:None, 2:None, 3:None, 4:None}
            for result in results:
                notas[result[2]][result[1]]=result[0]
            return True
        except Exception as error:
            print(error)
        finally:
            return notas

