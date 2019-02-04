import psycopg2 as database

class DatabaseConnection:

    @staticmethod
    def get_connection():
        connection =  database.connect(
            host="localhost",
            port=5432,
            database="escolar",
            user="postgres",
            password="123"
        )
        connection.autocommit = True
        return connection