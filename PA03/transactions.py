"""Keeps log of transactions"""
import sqlite3

class Transaction():
    """Keeps log of transactions"""
    def __init__(self, debug: bool = False, url: str='transaction.db'):
        """debug: if true, will reset all tables"""
        self.url = url
        if debug:
            # drop all tables
            self.run_query("TRUNCATE TABLE IF EXISTS transactions;", ())
            self.run_query("TRUNCATE TABLE IF EXISTS category;", ())
        self.run_query("""CREATE TABLE IF NOT EXISTS transactions (
            amount int, category_id int, year int, month int, day int, description varchar(50));
            """, ())
        self.run_query("""CREATE TABLE IF NOT EXISTS category (
            name varchar(20) UNIQUE NOT NULL
            );""", ())

    def get_categories(self):
        """Gets all catagories"""
        return self.run_query("SELECT rowid, * FROM category;", ())

    def create_category(self, catagory: str):
        """Creates a catagory"""
        self.run_query("INSERT INTO category values (?)", (catagory))

    def update_category(self, catagory_id: str):
        """Updates a catagory"""
        self.run_query("UPDATE catagory SET name=(?)", (catagory_id))

    def get_transaction(self):
        """Gets all transactions"""
        return self.run_query("SELECT * FROM transactions;", ())

    def get_transactions_by_year(self):
        """Gets all transactions ordered by year descending"""
        return self.run_query("SELECT * FROM transactions ORDER BY YEAR, MONTH, DAY DEC;", ())

    def get_transactions_by_month(self):
        """Gets transactions by month descending"""
        return self.run_query("SELECT * FROM transactions ORDER BY MONTH, DAY DEC;", ())

    def get_transaction_by_day(self):
        """Gets transactions ordered by day descending"""
        return self.run_query("SELECT * FROM transactions ORDER BY DAY DEC;", ())

    def create_transaction(self, transaction: dict):
        """Creates new Transaction: Takes dict with all transaction values as input"""
        if len(transaction) == 6:
            self.run_query("""
            INSERT INTO transactions VALUES (
                ?, ?, ?, ?, ?, ?
                )
                """, (v for v in transaction))

    def delete_transaction(self, transaction_id):
        """Deletes transaction by transaction_id"""
        self.run_query("DELETE FROM transactions WHERE rowid=(?)", (transaction_id,))


    def run_query(self, query, tuples):
        """Runs a query"""
        con = sqlite3.connect(self.url)
        cur = con.cursor()
        return cur.execute(query, tuples).fetchall()
