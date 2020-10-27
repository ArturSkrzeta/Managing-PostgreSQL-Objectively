import psycopg2
from dotenv import load_dotenv
from os import getenv


class Database:

    def __init__(self):

        load_dotenv()

        self.connection = psycopg2.connect(
                            host=getenv('DB_HOST'),
                            dbname=getenv('DB_NAME'),
                            port=getenv('DB_PORT'),
                            user=getenv('DB_USERNAME'),
                            password=getenv('DB_PASSWORD')
                        )
        self.cursor = self.connection.cursor()

    @classmethod
    def get_connection_status(cls, db):
        if isinstance(db, cls):
            return print("Connection Successful!")

    def create_table(self, table_name):
        qry = f'CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, name VARCHAR);'
        self.cursor.execute(qry)
        self.connection.commit()
        return print("A new Table created.")

    def insert(self, table_name, *values):
        self.cursor.execute(f"INSERT INTO {table_name} (name) VALUES ({','.join(['%s' for _ in values])});",values)
        self.connection.commit()

    def fetch_all(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def __del__(self):
        self.cursor.close()
        self.connection.close()
