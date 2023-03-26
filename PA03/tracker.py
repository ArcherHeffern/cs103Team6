from transactions import transaction

def print_job_menu():
    """print available jobs prompt"""
    jobs = ["0. quit",
    "1. show categories",
    "2. add category",
    "3. modify category",
    "4. show transactions",
    "5. add transaction",
    "6. delete transaction",
    "7. summarize transactions by date",
    "8. summarize transactions by month",
    "9. summarize transactions by year",
    "10. summarize transactions by category",
    "11. print this menu"]
    for prompt in jobs:
        print(prompt)

def get_job_request() -> int:
    """Get the numerical value for a prompt, return -1 if the input is invalid"""
    usr = input("Enter the number of a task to be completed: ").strip()
    if usr.isdigit():
        usr = int(usr)
        if usr >= 0 and usr <= 11:
            return usr
    return -1

def allocate_jobs(file: str):
    dbconn = Transaction(url = file)
    while True:
        task = get_job_request()
        if task == 0:
            break
        elif task == 1:
            print(dbconn.get_categories())
        elif task == 2:
            category = input("Enter a name for the category here: ")
            dbconn.create_category()
        elif task == 3:
            category = input("Enter a category here: ")
            category_id = dbconn.get_category_id(category)
            new_name = input("Enter a new name for the category here: ")
            dbconn.update_category(new_name,category_id)
        elif task == 4:
            print(dbconn.get_transactions())
        elif task == 5:
            amount = int(input("Enter amount here: "))
            category_id = dbconn.get_category_id(input("Enter category name here: "))
            year = int(input("Enter year here: "))
            month = int(input("Enter month here: "))
            day = int(input("Enter day here: "))
            description = input("Enter a description here: ")
            new_transaction = (amount,category_id,year,month,day,description)
            dbconn.create_transaction(new_transaction)
        elif task == 6:
            category = input("Enter the category to be deleted here: ")
            dbconn.delete_transaction()
        elif task == 7:
            print(dbconn.get_transactions_by_day())
        elif task == 8:
            print(dbconn.get_transactions_by_month())
        elif task == 9:
            print(dbconn.get_transactions_by_year())
        elif task == 10:
            category = input("Enter a category here: ")
            print(dbconn.get_transactions_by_category(category))
        elif task == 11:
            print_job_menu()
        else:
            print("Invalid input, no such operation exists")

"""
main method
"""
            
if __name__ == '__main__':
    print_job_menu()
    file = input("Enter database name here: ")
    allocate_jobs(file)
    
        
                
        
            
