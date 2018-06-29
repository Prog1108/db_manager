from db_manager import SqliteManager


if __name__ == '__main__':
    create_table_sql = """
    CREATE TABLE test_abcde(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER DEFAULT -1)
    """

    db_manager = SqliteManager()

    db_manager.create_table(create_table_sql, 'test.db')
