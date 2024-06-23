from mysql.connector.pooling import MySQLConnectionPool

from .utils import HOST, DATABASE, USUARIO_BANCO, SENHA_BANCO


class ConexaoBase:

    def __init__(self):

        self.pool = MySQLConnectionPool(
            pool_name='mypool',
            pool_size=5,
            pool_reset_session=True,
            user=USUARIO_BANCO,
            password=SENHA_BANCO,
            host=HOST,
            database=DATABASE,
        )

    def __enter__(self):
        self.conexao = self.pool.get_connection()
        return self.conexao

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conexao:
            self.conexao.close()
        if exc_type is not None:
            raise
