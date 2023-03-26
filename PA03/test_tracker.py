from transactions import Transaction
import sqlite3
import pytest

# before each test, we would like to create a transaction object, and pass it in to be used
@pytest.fixture
def db(tmp_path):
    yield tmp_path / 'test.db'

@pytest.fixture
def sample_data() -> tuple:
    """Sample data for transactions and catagories"""
    return  ([("15b",), ("35z",), ("17a",)] ,[(35, 1, 2003, 5, 7, "Bought big potato from store"), (2, 3, 2021, 3, 20, "A stick of gum"), (4, 2, 2003, 7, 8, "new house")])

@pytest.fixture(autouse=True)
def db_connect(db, sample_data):
    """Init db connection, and create test data"""
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (amount int, category_id int, year int, month int, day int, description varchar(50));")
    cur.execute("CREATE TABLE IF NOT EXISTS category (name varchar(10) UNIQUE NOT NULL);")
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



def test_get_catagory(db_connect: Transaction, sample_data: tuple):
    transaction = db_connect
    assert transaction.get_categories() == [(i+1, data[0]) for i, data in enumerate(sample_data[0])]


def test_post_catagory(db_connect: Transaction, sample_data: tuple):
    new_cat_name = "dfff3"
    db_connect.create_category(new_cat_name)
    assert db_connect.get_categories()[-1] == (len(sample_data[0]) + 1, new_cat_name)


def test_update_catagory(db_connect: Transaction, sample_data: tuple):
    new_cat_name = "dfff3"
    rowid = 3
    db_connect.update_category(new_cat_name, rowid)
    assert db_connect.get_categories()[-1] == (len(sample_data[0]), new_cat_name)


def test_show_transactions(db_connect: Transaction, sample_data: tuple):
    transactions = db_connect.get_transactions()
    assert transactions == [(i+1,) + (data) for i, data in enumerate(sample_data[1])]

def test_add_transactions(db_connect: Transaction, sample_data):
    new_transaction = ( 40, 3, 2005, 12, 1, "I bought a cat!")
    db_connect.create_transaction(new_transaction)
    assert db_connect.get_transactions()[-1] == (len(sample_data[1])+1,) + new_transaction


def test_delete_transactions(db_connect : Transaction, sample_data : tuple):
    db_connect.delete_transaction(3)
    assert db_connect.get_transactions() == [(i+1,) + (data) for i, data in enumerate(sample_data[1][:-1])]


def get_transactions_by_date(db_connect: Transaction, sample_data: tuple):
    day = db_connect.get_transaction_by_day()
    orderedData = ([(35, 1, 2003, 5, 7, "Bought big potato from store"), (2, 3, 2021, 3, 20, "A stick of gum"), (4, 2, 2003, 7, 8, "new house")])
    assert day == [(i+1,) + (data) for i, data in enumerate(orderedData[1][:-2])]

def get_transactions_by_month(db_connect: Transaction, sample_data: tuple):
    month = db_connect.get_transactions_by_month()
    orderedMonth = ([(35, 1, 2003, 5, 7, "Bought big potato from store"), (2, 3, 2021, 3, 20, "A stick of gum"), (4, 2, 2003, 7, 8, "new house")])
    assert month == [(i+1,) + (data) for i, data in enumerate(orderedMonth[1][:-3])]


def get_transactions_by_year(db_connect: Transaction, sample_data: tuple):
    pass


def get_transactions_by_catagory(db_connect: Transaction, sample_data: tuple):
    pass

