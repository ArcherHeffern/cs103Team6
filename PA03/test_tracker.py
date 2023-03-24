from transactions import Transaction
import sqlite3
import pytest

# before each test, we would like to create a transaction object, and pass it in to be used
@pytest.fixture
def db(tmp_path):
    yield tmp_path / 'test.db'

@pytest.fixture
def sample_data():
    """Sample data for transactions and catagories"""
    return  ([("15b",), ("35z",), ("17a",)] ,[(35, 1, 2003, 5, 7, "Bought big potato from store"), (2, 3, 2021, 3, 20, "A stick of gum"), (4, 2, 2003, 7, 8, "new house")])

@pytest.fixture(autouse=True)
def db_connect(db, sample_data):
    """Init db connection, and create test data"""
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (amount int, category int, year int, month int, day int, description varchar(50));")
    cur.execute("CREATE TABLE IF NOT EXISTS category (category varchar(10));")
    cur.executemany("INSERT INTO category VALUES (?);", sample_data[0])
    cur.executemany("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?);", sample_data[1])
    con.commit()
    transaction = Transaction(url=db)
    yield transaction
    cur.execute("DROP TABLE category")
    cur.execute("DROP TABLE transactions")
    con.commit()
    cur.close()
    con.close()



def test_get_catagory(db_connect: Transaction, sample_data):
    transaction = db_connect
    assert transaction.get_catagories() == [(i+1, data[0]) for i, data in enumerate(sample_data[0])]


def test_post_catagory():
    pass


def test_update_catagory():
    pass


def test_show_transactions():
    pass


def test_add_transactions():
    pass


def test_delete_transactions():
    pass


def get_transactions_by_date():
    pass


def get_transactions_by_month():
    pass


def get_transactions_by_year():
    pass


def get_transactions_by_catagory():
    pass