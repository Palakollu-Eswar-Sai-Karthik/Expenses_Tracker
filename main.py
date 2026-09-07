# List which contains user data
expenses = []

# All Functions
def design():
    for i in range(17):
        print("=",end="")
        
def AddExpense():
    user = {}
    length = len(expenses)
    user["id"]=length+1
    while True:
        try:
            amount = float(input("Enter your expense amount: "))
            if amount > 0:
                user["amount"]=amount
            break
        except ValueError:
            print("Please enter a valid number")        
    user["category"]=input("Enter the category of the expense: ")
    user["description"]=input("Enter the description of the expense: ")
    expenses.append(user)
    
def ViewExpenses():
    if len(expenses)==0:
        print("No expense found!")
    else:
        print("\n")
        design()
        print("\n   EXPENSES")
        design()
        print("\n")
        print("ID\tAmount\t\tCategory\t\tDescription")
        for i in expenses:
            print(f"{i['id']}\t{i['amount']}\t\t{i['category']}\t\t{i['description']}")
   
def UpdateExpense():
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
                    i["amount"]=float(input("Enter your expense amount: "))
                    break
                except ValueError:
                    print("Please enter a valid number")
            i["category"]=input("Enter the category of the expense: ")
            i["description"]=input("Enter the description of the expense: ")
            print("Expense updated successfully")
            break
    else:
        print("Id not found")

def DeleteExpense():
    while True:
        try:
            searchid = int(input("Enter the id of the expense: "))
            break
        except ValueError:
            print("Enter a valid ID")
    for i in expenses:
        if i["id"]==searchid:
            expenses.remove(i)
            print("Expense deleted successfully")
            break
    else:
        print("Id not found")

def ViewTotalExpenses():
    if len(expenses)==0:
        print("No expense found!")
    else:
        totalexpenses=0
        for i in expenses:
            totalexpenses+=i["amount"]
        print("No expense found!")

def FilterbyCategory():
    found = False
    filter = input("Enter the category: ")
    for i in expenses:
        if i["category"] == filter:
            found = True
            print(f"{i['id']}\t{i['amount']}\t\t{i['category']}\t\t{i['description']}")
    if not found:
        print("No category found!")
    
while(1):
    design()
    print("\n Expense Tracker")
    design()
    print("\n1. Add Expenses\n2. View Expenses\n3. Update Expense\n4. Delete Expense\n5. View Total Expenses\n6. Filter by Category\n7. Exit")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Enter a valid choice")
    match choice:
        case 1:
            AddExpense()
        case 2:
            ViewExpenses()
        case 3:
            UpdateExpense()
        case 4:
            DeleteExpense()
        case 5:
            ViewTotalExpenses()
        case 6:
            FilterbyCategory()
        case 7:
            print("Thankyou for using Expense Tracker!")
            break
        case _:
            print("Invalid choice. Please try again.")