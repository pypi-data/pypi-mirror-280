from mysql.connector.errors import DatabaseError
from .connection import ConexaoBase


class InsertBD(ConexaoBase):
    def insert(self, query: str, params: tuple = ()):
        with self as conexao:
            cursor = conexao.cursor()
            try:
                cursor.execute(query, params)
                conexao.commit()
                return True
            except DatabaseError as error:
                return error.msg
