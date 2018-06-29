import re
import sqlite3


create_table_sql = """
CREATE TABLE test(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER DEFAULT -1,
)"""


class SqliteManager(object):
    def __init__(self):
        self.cursor = None
        self.table_name = None

    def create_table(self, sql, db_name):
        pattern = r'\n.*.CREATE TABLE '
        match_text = re.search(pattern, sql)
        sub_sql = sql[match_text.end():]
        pattern = r'\('
        match_text = re.search(pattern, sub_sql)
        table_name = sub_sql[:match_text.start()]
        print(table_name)

        """
        table_name = sub_sql[:match_text.end()+1]
        print(table_name)

        self.table_name = table_name
        db = sqlite3.connect(table_name)
        self.cursor = db.cursor()
        self.cursor.execute(sql)

    def insert_into(self, *values)
        sql = 'INSERT INTO ' + self.table_name +
        """
