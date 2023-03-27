"""Keeps log of transactions"""
import sqlite3

class Transaction():
    """Keeps log of transactions"""
    def __init__(self, debug: bool = False, url: str='transaction.db'):
        """debug: if true, will reset all tables"""
        self.url = url
        self.query_transactions: str = """SELECT
        transactions.rowid, amount, category.name, year, month, day, description 
        FROM transactions 
        INNER JOIN category 
        ON transactions.category_id=category.rowid {};"""
        if debug:
            # drop all tables
            self.run_query("DROP TABLE IF EXISTS transactions;", ())
            self.run_query("DROP TABLE IF EXISTS category;", ())
        self.run_query("""CREATE TABLE IF NOT EXISTS transactions (
            amount int, category_id int, year int, month int, day int, description varchar(50));
            """, ())
        self.run_query("""CREATE TABLE IF NOT EXISTS category (
            name varchar(20) UNIQUE NOT NULL
            );""", ())


    def get_categories(self):
        """Gets all catagories"""
        return self.run_query("SELECT rowid, * FROM category;", ())


    def create_category(self, category: str):
        """Creates a category"""
        self.run_query("INSERT INTO category values (?)", (category,))


    def update_category(self, newname: str, category_id: int):
        """Updates a category"""
        self.run_query("UPDATE category SET name=(?) WHERE rowid=(?)", (newname, category_id))


    def get_transactions(self):
        """Gets all transactions"""
        return self.run_query(self.query_transactions.format(""), ())


    def get_transactions_by_year(self):
        """Gets all transactions ordered by year descending"""
        return self.run_query(self.query_transactions.format("""ORDER BY
        YEAR DESC, MONTH DESC, DAY DESC"""), ())


    def get_transactions_by_month(self):
        """Gets transactions by month descending"""
        return self.run_query(self.query_transactions.format("ORDER BY MONTH DESC, DAY DESC"), ())


    def get_transactions_by_day(self):
        """Gets transactions ordered by day descending"""
        return self.run_query(self.query_transactions.format("ORDER BY DAY DESC"), ())

    def get_transactions_by_category(self, category: str):
        """get transaction information for specific category name"""
        category_id = self.get_category_id(category)
        if len(category_id) == 0:
            return []
        return self.run_query("SELECT * FROM transactions WHERE rowid=(?)", (category_id[0],))

    def create_transaction(self, transaction: tuple):
        """Creates new Transaction: Takes tuple with all transaction values as input"""
        if len(transaction) == 6:
            self.run_query("""
            INSERT INTO transactions VALUES (
                ?, ?, ?, ?, ?, ?
                )
                """, transaction)

    def get_category_id(self,category: str):
        """Get the rowid for a specified category"""
        return self.run_one_query("SELECT rowid FROM category WHERE name = (?)", (category,))

    def delete_transaction(self, category_id):
        """Deletes transaction by rowid"""
        self.run_query("DELETE FROM transactions WHERE rowid=(?)", (category_id,))

# delete all transactions by catagory

    def run_query(self, query, tuples):
        """Runs a query"""
        con = sqlite3.connect(self.url)
        cur = con.cursor()
        values = cur.execute(query, tuples).fetchall()
        con.commit()
        return values

    def run_one_query(self, query, tuples):
        """Runs a query"""
        con = sqlite3.connect(self.url)
        cur = con.cursor()
        values = cur.execute(query, tuples).fetchone()
        con.commit()
        return values
