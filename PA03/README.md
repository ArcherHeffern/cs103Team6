# PA03

create a transcript of your session as you demonstrate each of the features you have implemented. 
create a README.md file which describes your app and contains 
* a script of you running pylint
```bash
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

* then running pytest, and 
```bash
(cosi103) archers-air:PA03 archerheffern$ pytest -v
==================================================== test session starts =====================================================
platform darwin -- Python 3.11.0, pytest-7.1.2, pluggy-1.0.0 -- /Users/archerheffern/miniconda3/envs/cosi103/bin/python
cachedir: .pytest_cache
rootdir: /Users/archerheffern/Desktop/Code/Projects/cs103Team6/PA03
collected 10 items                                                                                                           

test_tracker.py::test_get_catagory PASSED                                                                              [ 10%]
test_tracker.py::test_post_catagory PASSED                                                                             [ 20%]
test_tracker.py::test_update_catagory PASSED                                                                           [ 30%]
test_tracker.py::test_show_transactions PASSED                                                                         [ 40%]
test_tracker.py::test_add_transactions PASSED                                                                          [ 50%]
test_tracker.py::test_delete_transactions PASSED                                                                       [ 60%]
test_tracker.py::test_get_transactions_by_day PASSED                                                                   [ 70%]
test_tracker.py::test_get_transactions_by_month PASSED                                                                 [ 80%]
test_tracker.py::test_get_transactions_by_year PASSED                                                                  [ 90%]
test_tracker.py::test_get_transactions_by_catagory PASSED                                                              [100%]

===================================================== 10 passed in 0.07s =====================================================
```

* then running tracker.py and demonstrating all of the features you added

(cosi103) archers-air:PA03 archerheffern$ python tracker.py 
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
Enter the number of a task to be completed: 1
hello   fishing turtle  asdkjf  asdfadsfs
Enter the number of a task to be completed: 2
Enter a name for the category here: newcatagory
Enter the number of a task to be completed: 1
hello   fishing turtle  asdkjf  asdfadsfs       newcatagory
Enter the number of a task to be completed: 3
Which category would you like to rename: newcatagory
New name: newnewcatagory
Enter the number of a task to be completed: 1
hello   fishing turtle  asdkjf  asdfadsfs       newnewcatagory
Enter the number of a task to be completed: 4
--------------------
rowid: 2
price: $50
Category: hello
Date: 20/20/2000
Description: this is my test transaction
--------------------
Enter the number of a task to be completed: 5
Enter amount here: 50
Enter category name here: hello
Enter year here: 2021
Enter month here: 3
Enter day here: 17
Enter a description here: this is my test transaction 2
Enter the number of a task to be completed: 4
--------------------
rowid: 2
price: $50
Category: hello
Date: 20/20/2000
Description: this is my test transaction
-------------------- --------------------
rowid: 3
price: $50
Category: hello
Date: 3/17/2021
Description: this is my test transaction 2
--------------------
Enter the number of a task to be completed: 6
Enter the transaction to be deleted here: 2
Enter the number of a task to be completed: 4
--------------------
rowid: 3
price: $50
Category: hello
Date: 3/17/2021
Description: this is my test transaction 2
--------------------
Enter the number of a task to be completed: 7
--------------------
rowid: 3
price: $50
Category: hello
Date: 3/17/2021
Description: this is my test transaction 2
--------------------
Enter the number of a task to be completed: 8
--------------------
rowid: 3
price: $50
Category: hello
Date: 3/17/2021
Description: this is my test transaction 2
--------------------
Enter the number of a task to be completed: 9
--------------------
rowid: 3
price: $50
Category: hello
Date: 3/17/2021
Description: this is my test transaction 2
--------------------
Enter the number of a task to be completed: 10
Enter a category here: hello
--------------------
rowid: 3
price: $50
Category: hello
Date: 3/17/2021
Description: this is my test transaction 2
--------------------
Enter the number of a task to be completed: 11
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
Enter the number of a task to be completed: 0