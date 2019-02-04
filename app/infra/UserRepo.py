from app.infra import DatabaseConnection as db
from app.models.User import User


class UserRepo:
    def __init__(self):
        self.__connection = db.DatabaseConnection.get_connection()

    def add_user(self, user):
        insert_sql = "INSERT INTO usuario (nome, cpf, email, senha, tipo_usuario, telefone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
        try:
            cursor = self.__connection.cursor()
            cursor.execute(insert_sql % (user.nome, user.cpf, user.email, user.senha, user.tipo, user.telefone))
            return True
        except Exception as error:
            print(error)
            return False

    def get_users(self):
        get_sql = "SELECT cod, nome, cpf, email, senha, tipo_usuario, telefone FROM usuario"
        user_list = []
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql)
            results = cursor.fetchall()
            for result in results:
                user_list.append(User(result[0], result[1], result[2], result[3], result[4], result[5], [result[6]]))
        except Exception as error:
            print("Error: {0}".format(error))
        finally:
            return user_list

    def get_user(self, user_email):
        get_sql = "SELECT cod, nome, cpf, email, senha, tipo_usuario, telefone FROM usuario WHERE email = '%s'"
        user = None
        try:
            cursor = self.__connection.cursor()
            cursor.execute(get_sql %(user_email))
            result = cursor.fetchone()
            user = User(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
        except Exception as error:
            raise("Error: {0}".format(error))
        finally:
            return user
