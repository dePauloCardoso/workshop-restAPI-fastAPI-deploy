import psycopg2

class PostgreSQLConnection:
    def __ini__(self, dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
            print('Conexão com sucesso!')
        except psycopg2.Error as e:
            print('Erro ao conectar ao Postgre:', e)

    def select_user(self, query):
        if not self.conn:
            print('Você não está conectado.')
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2 as e:
            print('Erro ao executar a consulta', e)
            return None 

    def insert_user():
        pass

    def delete_user():
        pass

    def update_user():
        pass

    def close():
        pass