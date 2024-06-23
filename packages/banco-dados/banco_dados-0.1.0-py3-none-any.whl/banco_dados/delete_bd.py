from .connection import ConexaoBase


class Delete(ConexaoBase):
    def delete(self, query: str, params: tuple = ()) -> None:
        with self as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, params)
            conexao.commit()