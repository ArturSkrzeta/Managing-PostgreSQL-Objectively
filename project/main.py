from database import Database
from sys import argv


def connect_to_db():
    db = Database()
    Database.get_connection_status(db)
    return db

def main():

    db = connect_to_db()
    table_name = 'clients'

    # python main.py setup
    if len(argv) > 1 and argv[1] == 'setup':
        db.create_table(table_name)

    # python main.py add name
    if len(argv) > 1 and argv[1] == 'add':
        name = argv[2]
        db.insert(table_name, name)

    # python main.py list
    if len(argv) > 1 and argv[1] == 'list':
        db.fetch_all(table_name)

if __name__ == "__main__":
    main()
