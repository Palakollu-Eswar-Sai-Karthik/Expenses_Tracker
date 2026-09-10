import mysql.connector
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="karthik@1011",
            database="expense_tracker"
        )
        self.cursor = self.connection.cursor()
        
    def load_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        rows = self.cursor.fetchall()
        expenses = []
        for row in rows:
            expense = {
                "id": row[0],
                "amount": row[1],
                "category": row[2],
                "description": row[3]
            }
            expenses.append(expense)
        return expenses

    def add_expense(self, amount, category, description):
        query = """
            INSERT INTO expenses (amount, category, description)
            VALUES (%s, %s, %s)
        """
        values = (amount, category, description)
        self.cursor.execute(query, values)
        self.connection.commit()

    def update_expense(self, expense_id, amount, category, description):
        query = """
            UPDATE expenses
            SET amount = %s, category = %s, description = %s
            WHERE id = %s
        """
        values = (amount, category, description, expense_id)
        self.cursor.execute(query, values)
        if self.cursor.rowcount:
            self.connection.commit()
            return True
        return False
    
    def delete_expense(self, expense_id):
        query = "DELETE FROM expenses WHERE id = %s"
        values = (expense_id,)
        self.cursor.execute(query, values)
        if self.cursor.rowcount:
            self.connection.commit()
            return True
        return False
    
    def get_total_expenses(self):
        query = "SELECT SUM(amount) FROM expenses"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]
    
    def filter_by_category(self, category):
        query = "SELECT * FROM expenses WHERE category = %s"
        values = (category,)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def search_expenses(self, search_word):
        search_pattern = f"%{search_word}%"
        query = """
            SELECT * FROM expenses
            WHERE category LIKE %s
            OR description LIKE %s
        """
        values = (search_pattern, search_pattern)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.connection.close()
    
class ExpenseTracker:
    def __init__(self):
        self.database = Database()
    def design(self):
        for _ in range(17):
            print("=", end="")
    def add_expense(self):
        while True:
            try:
                amount = float(input("Enter your expense amount: "))
                if amount > 0:
                    break
                print("Amount must be greater than 0")
            except ValueError:
                print("Please enter a valid number")
        while True:
            category = input("Enter the category of the expense: ")
            if category:
                category = category.lower()
                break
            print("Category cannot be empty")
        while True:
            description = input("Enter the description of the expense: ")
            if description:
                break
            print("Description cannot be empty")
        self.database.add_expense(amount,category,description)
        print("Expense added successfully!")

    def view_expenses(self):
        expenses = self.database.load_expenses()
        if not expenses:
            print("No expense found!")
            return
        print("\n")
        self.design()
        print("\n   EXPENSES")
        self.design()
        print("\n")
        print(f"{'ID':<5}{'Amount':<12}{'Category':<15}{'Description'}")
        for expense in expenses:
            print(f"{expense['id']:<5}{expense['amount']:<12}{expense['category']:<15}{expense['description']}")

    def update_expense(self):
        while True:
            try:
                expense_id = int(input("Enter the id of the expense: "))
                break
            except ValueError:
                print("Enter a valid ID")
        expenses = self.database.load_expenses()
        selected_expense = None
        for expense in expenses:
            if expense["id"] == expense_id:
                selected_expense = expense
                break
        if selected_expense is None:
            print("Id not found")
            return
        while True:
            try:
                amount = float(input("Enter your expense amount: "))
                if amount > 0:
                    break
                print("Amount must be greater than 0")
            except ValueError:
                print("Please enter a valid number")
        while True:
            category = input("Enter the category of the expense: ")
            if category:
                category = category.lower()
                break
            print("Category cannot be empty")
        while True:
            description = input("Enter the description of the expense: ")
            if description:
                break
            print("Description cannot be empty")
        updated = self.database.update_expense(expense_id,amount,category,description)
        if updated:
            print("Expense updated successfully")
        else:
            print("Id not found")

    def delete_expense(self):
        while True:
            try:
                expense_id = int(input("Enter the id of the expense: "))
                break
            except ValueError:
                print("Enter a valid ID!")
        deleted = self.database.delete_expense(expense_id)
        if deleted:
            print("Expense deleted successfully")
        else:
            print("Id not found!")

    def view_total_expenses(self):
        total = self.database.get_total_expenses()
        if total is None:
            print("No expense found!")
        else:
            print(f"Total Expenses: {total}")

    def filter_by_category(self):
        category = input("Enter the category: ").lower()
        rows = self.database.filter_by_category(category)
        if not rows:
            print("No category found!")
            return
        for expense in rows:
            print(f"{expense[0]:<5}{expense[1]:<12}{expense[3]}{expense[2]:<15}")

    def search_expense(self):
        while True:
            search_word = input("Enter search keyword: ").lower()
            if search_word:
                break
            print("Search word cannot be empty")
        rows = self.database.search_expenses(search_word)
        if not rows:
            print("No matching expense found!")
            return
        for expense in rows:
            print(f"{expense[0]:<5}{expense[1]:<12}{expense[2]:<15}{expense[3]}")

    def run(self):
        while True:
            self.design()
            print("\n Expense Tracker")
            self.design()
            print(
                "\n1. Add Expenses"
                "\n2. View Expenses"
                "\n3. Update Expense"
                "\n4. Delete Expense"
                "\n5. View Total Expenses"
                "\n6. Filter by Category"
                "\n7. Search Expense"
                "\n8. Exit"
            )
            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("Enter a valid choice")
            match choice:
                case 1:
                    self.add_expense()
                case 2:
                    self.view_expenses()
                case 3:
                    self.update_expense()
                case 4:
                    self.delete_expense()
                case 5:
                    self.view_total_expenses()
                case 6:
                    self.filter_by_category()
                case 7:
                    self.search_expense()
                case 8:
                    print("Thankyou for using Expense Tracker!")
                    self.database.close()
                    break
                case _:
                    print("Invalid choice. Please try again.")
app = ExpenseTracker()
app.run()