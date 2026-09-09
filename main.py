# import functions
import json

# File Name
FILE_NAME = "storage.json"

# Loading json data into code
def load_expenses():
    try:
        with open(FILE_NAME,"r",encoding="utf-8") as file:
            return json.load(file) 
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Storing the data into json
def save_expenses():
    with open(FILE_NAME,"w",encoding="utf-8") as file:
        json.dump(expenses,file,indent=4)

# All Functions
def design():
    for _ in range(17):
        print("=",end="")

def max_id()->int:
    max_value = 0
    for expense in expenses:
        if expense["id"] > max_value:
            max_value = expense["id"]
    return max_value
        
def add_expense():
    user = {}
    id_value = max_id()
    user["id"] = id_value + 1
    while True:
        try:
            amount = float(input("Enter your expense amount: "))
            if amount > 0:
                user["amount"]=amount
                break
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Please enter a valid number") 
    while True:       
        category=input("Enter the category of the expense: ")
        if category:
            user["category"] = category.lower()
            description=input("Enter the description of the expense: ")
            if description:
                user["description"] = description
                break
            else:
                print("Description cannot be empty")
        else:
            print("Category cannot be empty")
    expenses.append(user)
    save_expenses()
    
def view_expenses():
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
    while True:
        try:
            searchid = int(input("Enter the id of the expense: "))
            break
        except ValueError:
            print("Enter a valid ID")
    for i in expenses:
        if i["id"]==searchid:
            while True:
                try:
                    updatedamount=float(input("Enter your expense amount: "))
                    if updatedamount>0:
                        i["amount"] = updatedamount
                        break
                    else:
                        print("Amount must be greater than 0")
                except ValueError:
                    print("Please enter a valid number")
            while True:       
                updatedcategory=input("Enter the category of the expense: ")
                if updatedcategory:
                    i["category"]= updatedcategory.lower()
                    updateddescription=input("Enter the description of the expense: ")
                    if updateddescription:
                        i["description"] = updateddescription
                        break
                    else:
                        print("Description cannot be empty")
                else:
                    print("Category cannot be empty")
            print("Expense updated successfully")
            break
    else:
        print("Id not found")
    save_expenses()

def delete_expense():
    while True:
        try:
            searchid = int(input("Enter the id of the expense: "))
            break
        except ValueError:
            print("Enter a valid ID!")
    for expense in expenses:
        if expense["id"]==searchid:
            expenses.remove(expense)
            print("Expense deleted successfully")
            break
    else:
        print("Id not found!")
    save_expenses()

def view_total_expenses():
    if not expenses:
        print("No expense found!")
    else:
        totalexpenses=0
        for expense in expenses:
            totalexpenses+= expense ["amount"]
        print(f"Total Expenses: {totalexpenses}")

def filter_by_category():
    found = False
    search_category = input("Enter the category: ").lower()
    for expense in expenses:
        if expense["category"] == search_category:
            found = True
            print(f"{expense['id']:<5}{expense['amount']:<12}{expense['category']:<15}{expense['description']}")
    if not found:
        print("No category found!")

def search_expense():
    found = False
    while True:
        search_word = input("Enter search keyword: ").lower()
        if search_word:
            break
        else:
            print("Search word cannot be empty")
    for expense in expenses:
        if search_word in expense["category"] or search_word in expense["description"]:
            found = True
            print(f"{expense['id']:<5}{expense['amount']:<12}{expense['category']:<15}{expense['description']}")
    if not found:
        print("No matching expense found!")
        return
# List which contains user data
expenses = load_expenses()

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