from .connection import ConexaoBase


class SelectBD(ConexaoBase):
    def select(self, query: str, params: tuple = ()) -> dict:
        with self as conexao:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchall()

    def select_one(self, query: str, params: tuple = ()) -> dict:
        with self as conexao:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchone()