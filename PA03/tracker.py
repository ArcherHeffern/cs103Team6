from transactions import Transaction

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

def print_job_menu():
    """print available jobs prompt"""
    print("\n".join(jobs))

def get_job_request() -> int:
    """Get the numerical value for a prompt, return -1 if the input is invalid"""
    usr = input("Enter the number of a task to be completed: ").strip()
    if usr.isdigit():
        usr = int(usr)
        if usr >= 0 and usr <= 11:
            return usr
    return -1

def transactions_to_string(transactions: list):
    """Takes a tuple of transactions as input and returns string representation"""
    output = []
    for t in transactions:
        if len(t) != 7:
            continue
        output.append("\n".join(["-"*20, "rowid: " + str(t[0]), "price: $" +str(t[1]), "Category: " + t[2], "Date: " + str(t[4]).strip() + "/" + str(t[5]).strip() + "/" + str(t[3]).strip(), "Description: " + t[6], "-"*20]))
    return " ".join(output)

def allocate_jobs():
    dbconn = Transaction()
    while True:
        task = get_job_request()
        if task == 0:
            break
        elif task == 1:
            # Show categories
            categories = dbconn.get_categories()
            for i, category in enumerate(categories):
                categories[i] = str(category[1])
            print("\t".join(categories))
        elif task == 2:
            # Add category
            category = input("Enter a name for the category here: ")
            try:
                dbconn.create_category(category)
            except:
                print("Category already exists")
        elif task == 3:
            # Modify category
            category = input("Which category would you like to rename: ")
            if len(category) == 0:
                print("Category does not exist")
            else:
                category_id = dbconn.get_category_id(category)
                if len(category_id) == 0:
                    print("Category does not exist")
                else:
                    category_id = category_id[0]
                    new_name = input("New name: ")
                    try:
                        dbconn.update_category(new_name,category_id)
                    except:
                        print("Category already exists")
        elif task == 4:
            transactions = dbconn.get_transactions()
            print(transactions_to_string(transactions))
        elif task == 5:
            amount = int(input("Enter amount here: "))
            category_id = dbconn.get_category_id(input("Enter category name here: "))
            if len(category_id) == 0:
                print("Category does not exist")
                continue
            category_id = category_id[0]
            year = int(input("Enter year here: "))
            month = int(input("Enter month here: "))
            day = int(input("Enter day here: "))
            description = input("Enter a description here: ")
            new_transaction = (amount,category_id,year,month,day,description)
            dbconn.create_transaction(new_transaction)
        elif task == 6:
            tranaction = input("Enter the transaction to be deleted here: ")
            dbconn.delete_transaction(tranaction)
        elif task == 7:
            print(transactions_to_string(dbconn.get_transactions_by_day()))
        elif task == 8:
            print(transactions_to_string(dbconn.get_transactions_by_month()))
        elif task == 9:
            print(transactions_to_string(dbconn.get_transactions_by_year()))
        elif task == 10:
            category = input("Enter a category here: ")
            try:
                print(transactions_to_string(dbconn.get_transactions_by_category(category)))
            except:
                print("Category does not exist")
        elif task == 11:
            print_job_menu()
        else:
            print("Invalid input, no such operation exists")

"""
main method
"""
            
if __name__ == '__main__':
    print_job_menu()
    allocate_jobs()
    
        
                
        
            
