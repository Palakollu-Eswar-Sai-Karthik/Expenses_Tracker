# import functions
import mysql.connector

# Creating connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sk@1011",
    database="expense_tracker"
)

# Cursor is mediator btwn code and database
cursor = connection.cursor()

# All Functions
# Loading data into code
def load_expenses():
    cursor.execute("select * from expenses")
    rows = cursor.fetchall()
    expenses = []
    for row in rows:
        expense = {
            "id":row[0],
            "amount":row[1],
            "category":row[2],
            "description":row[3]
        }
        expenses.append(expense)
    return expenses

# design 
def design():
    for _ in range(17):
        print("=",end="")
        
def add_expense():
    while True:
        try:
            amount = float(input("Enter your expense amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Please enter a valid number") 
    while True:       
        category=input("Enter the category of the expense: ")
        if category:
            category = category.lower()
            description=input("Enter the description of the expense: ")
            if description:
                break
            else:
                print("Description cannot be empty")
        else:
            print("Category cannot be empty")
    query = """insert into expenses(amount,category,description)
                values(%s,%s,%s)"""
    values = (amount,category,description)
    cursor.execute(query,values)
    connection.commit()
    print("Expense added successfully!")
    
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expense found!")
    else:
        print("\n")
        design()
        print("\n   EXPENSES")
        design()
        print("\n")
        print(f"{'ID':<5}{'Amount':<12}{'Category':<15}{'Description'}")
        for expense in expenses:
            print(f"{expense['id']:<5}{expense['amount']:<12}{expense['category']:<15}{expense['description']}")
   
def update_expense():
    expenses = load_expenses()
    while True:
        try:
            searchid = int(input("Enter the id of the expense: "))
            break
        except ValueError:
            print("Enter a valid ID")
    for expense in expenses:
        if expense["id"]==searchid:
            while True:
                try:
                    updatedamount=float(input("Enter your expense amount: "))
                    if updatedamount>0:
                        expense["amount"] = updatedamount
                        break
                    else:
                        print("Amount must be greater than 0")
                except ValueError:
                    print("Please enter a valid number")
            while True:       
                updatedcategory=input("Enter the category of the expense: ")
                if updatedcategory:
                    expense["category"]= updatedcategory.lower()
                    updateddescription=input("Enter the description of the expense: ")
                    if updateddescription:
                        expense["description"] = updateddescription
                        break
                    else:
                        print("Description cannot be empty")
                else:
                    print("Category cannot be empty")
            query = """update expenses set amount=%s,category=%s,description=%s where id = %s"""
            values = (expense["amount"],expense["category"],expense["description"],searchid)
            cursor.execute(query,values)
            connection.commit()
            print("Expense updated successfully")
            break
    else:
        print("Id not found")
    
def delete_expense():
    while True:
        try:
            searchid = int(input("Enter the id of the expense: "))
            break
        except ValueError:
            print("Enter a valid ID!")
    query = "DELETE FROM expenses WHERE id = %s" 
    values = (searchid,)
    cursor.execute(query, values) 
    if cursor.rowcount: 
        connection.commit() 
        print("Expense deleted successfully") 
    else: print("Id not found!")

def view_total_expenses():
    query = "select sum(amount) from expenses"
    cursor.execute(query)
    result = cursor.fetchone()
    if result[0] is None:
        print('No expense found!')
    else:
        print(f"Total Expenses: {result[0]}")

def filter_by_category():
    search_category = input("Enter the category: ").lower()
    query = "select * from expenses where category = %s"
    values = (search_category,)
    cursor.execute(query,values)
    rows = cursor.fetchall()
    if not rows:
        print("No category found!")
    else:
        for expense in rows:
            print(f"{expense[0]:<5}{expense[1]:<12}{expense[2]:<15}{expense[3]}")

def search_expense():
    while True:
        search_word = input("Enter search keyword: ").lower()
        if search_word:
            break
        else:
            print("Search word cannot be empty")
    search_pattern = f"%{search_word}%"
    query = """select * from expenses
                where category Like %s or description like %s
            """
    values = (search_pattern,search_pattern)
    cursor.execute(query,values)
    rows = cursor.fetchall()
    if not rows:
        print("No matching expense found!")
    else:
        for expense in rows:
            print(f"{expense[0]:<5}{expense[1]:<12}{expense[2]:<15}{expense[3]}")

while True:
    design()
    print("\n Expense Tracker")
    design()
    print("\n1. Add Expenses\n2. View Expenses\n3. Update Expense\n4. Delete Expense\n5. View Total Expenses\n6. Filter by Category\n7. Search Expense\n8. Exit")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Enter a valid choice")
    match choice:
        case 1:
            add_expense()
        case 2:
            view_expenses()
        case 3:
            update_expense()
        case 4:
            delete_expense()
        case 5:
            view_total_expenses()
        case 6:
            filter_by_category()
        case 7:
            search_expense()
        case 8:
            print("Thankyou for using Expense Tracker!")
            break
        case _:
            print("Invalid choice. Please try again.")