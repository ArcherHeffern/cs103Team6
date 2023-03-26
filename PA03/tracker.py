"""
Main method
"""

def getJobRequest() -> int:
    usr = input("Enter the number of a task to be completed: ").strip()
    if usr.isdigit():
        usr = int(usr)
        if usr >= 0 and usr <= 11:
            return usr
    return -1

  
if __name__ == '__main__':
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
    task = 0
    while True:
        task = getJobRequest()
        if task = -1:
            print("Invalid input, no such operation exists")
        else:
            
        
            
