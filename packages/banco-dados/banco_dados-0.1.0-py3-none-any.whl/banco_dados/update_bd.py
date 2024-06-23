from .connection import ConexaoBase


class UpdateBD(ConexaoBase):
    def update(self, query: str, params: tuple = ()) -> None:
        with self as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, params)
            conexao.commit()
