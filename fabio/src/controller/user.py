
from fabio.src.db.connection import PostgreSQLConnection


db = PostgreSQLConnection(dbname='postgres', user='myuser', password='mypassword')

async def c_get_user(user_id: int):
    db.connect()
    user = db.execute_query(f'SELECT * FROM users WHERE id = {user_id}')
    db.close()
    return user