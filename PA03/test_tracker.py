from transactions import Transaction
import pytest

# before each test, we would like to create a transaction object, and pass it in to be used
@pytest.fixture
def db(tmp_path):
    """Archer - Creates temp path to db"""
    yield tmp_path / 'test.db'

@pytest.fixture
def sample_data() -> tuple:
    """Archer - Sample data for transactions and catagories"""
    return  ([("15b",), ("35z",), ("17a",)] ,[(35, 1, 2003, 5, 7, "Bought big potato from store"), (2, 3, 2021, 3, 20, "A stick of gum"), (4, 2, 2003, 7, 8, "new house")])

@pytest.fixture(autouse=True)
def db_connect(db, sample_data):
    """Archer - Init db connection, and create test data"""
    transaction: Transaction = Transaction(url=db, debug=True)
    for item in sample_data[0]:
        transaction.run_query("INSERT INTO category VALUES (?);", item)
    for item in sample_data[1]:
        transaction.run_query("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?);", item)
    yield transaction


def test_get_catagory(db_connect: Transaction, sample_data: tuple):
    """Archer"""
    assert db_connect.get_categories() == [(i+1, data[0]) for i, data in enumerate(sample_data[0])]


def test_post_catagory(db_connect: Transaction, sample_data: tuple):
    """Archer"""
    new_cat_name = "dfff3"
    db_connect.create_category(new_cat_name)
    assert db_connect.get_categories()[-1] == (len(sample_data[0]) + 1, new_cat_name)


def test_update_catagory(db_connect: Transaction, sample_data: tuple):
    """Archer"""
    new_cat_name = "dfff3"
    rowid = 3
    db_connect.update_category(new_cat_name, rowid)
    assert db_connect.get_categories()[-1] == (len(sample_data[0]), new_cat_name)


def test_show_transactions(db_connect: Transaction):
    """Archer"""
    transactions = db_connect.get_transactions()
    assert transactions == [(1, 35, "15b", 2003, 5, 7, "Bought big potato from store"), (2, 2, "17a", 2021, 3, 20, "A stick of gum"), (3, 4, "35z", 2003, 7, 8, "new house")]

def test_add_transactions(db_connect: Transaction):
    """Archer"""
    new_transaction = ( 40, 3, 2005, 12, 1, "I bought a cat!")
    db_connect.create_transaction(new_transaction)
    assert db_connect.get_transactions()[-1] == ( 4, 40, "17a", 2005, 12, 1, "I bought a cat!")


def test_delete_transactions(db_connect : Transaction):
    """Archer"""
    transaction = (2, 2, "17a", 2021, 3, 20, "A stick of gum")
    db_connect.delete_transaction(3)
    assert db_connect.get_transactions()[-1] == transaction


def test_get_transactions_by_day(db_connect: Transaction):
    """Archer and Paras"""
    orderedDay = [(2, 2, "17a", 2021, 3, 20, "A stick of gum"), (3, 4, "35z", 2003, 7, 8, "new house"), (1, 35, "15b", 2003, 5, 7, "Bought big potato from store")]
    assert db_connect.get_transactions_by_day() == orderedDay

def test_get_transactions_by_month(db_connect: Transaction):
    """Archer and Paras"""
    orderedMonth = [(3, 4, "35z", 2003, 7, 8, "new house"), (1, 35, "15b", 2003, 5, 7, "Bought big potato from store"), (2, 2, "17a", 2021, 3, 20, "A stick of gum")]
    assert db_connect.get_transactions_by_month() == orderedMonth


def test_get_transactions_by_year(db_connect: Transaction):
    """Archer"""
    orderedYear = [(2, 2, "17a", 2021, 3, 20, "A stick of gum"), (3, 4, "35z", 2003, 7, 8, "new house"), (1, 35, "15b", 2003, 5, 7, "Bought big potato from store")]
    assert db_connect.get_transactions_by_year() == orderedYear


def test_get_transactions_by_catagory(db_connect: Transaction):
    """Archer"""
    assert db_connect.get_category_id("15b") == (1,)
    assert db_connect.get_transactions_by_category("15b") == [(35, 1, 2003, 5, 7, "Bought big potato from store")]
