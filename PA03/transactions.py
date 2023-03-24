import sqlite3

class Transaction():
    def __init__(self, debug: bool = False, url: str='transaction.db'):
        """debug: if true, will reset all tables"""
        self.url = url
        if debug:
            # drop all tables
            self.runQuery("TRUNCATE TABLE IF EXISTS transactions;", ())
            self.runQuery("TRUNCATE TABLE IF EXISTS category;", ())
        self.runQuery("CREATE TABLE IF NOT EXISTS transactions (amount int, category_id int, year int, month int, day int, description varchar(50));", ())
        self.runQuery("CREATE TABLE IF NOT EXISTS category (name varchar(20) UNIQUE NOT NULL);", ())

    def get_catagories(self):
        """Gets all catagories"""
        return self.runQuery("SELECT * FROM category;", ())

    def create_catagory(self, catagory: str):
        """Creates a catagory"""
        self.runQuery("INSERT INTO category values (?)", (catagory))

    def runQuery(self, query, tuple):
        con = sqlite3.connect(self.url)
        cur = con.cursor()
        return cur.execute(query, tuple).fetchall()
