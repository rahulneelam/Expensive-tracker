# Import required libraries
import datetime
import json
import os

# Define ExpenseTracker class
class ExpenseTracker:
    # Initialize ExpenseTracker with filename
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    # Load expenses from JSON file
    def load_expenses(self):
        # Check if file exists
        if os.path.exists(self.filename):
            # Open file and load JSON data
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            # Return default expenses structure
            return {
                "categories": {},
                "monthly_summary": {}
            }

    # Save expenses to JSON file
    def save_expenses(self):
        # Open file and dump JSON data
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file)

    # Add new expense
    def add_expense(self):
        # Get user input
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        # Check if category exists
        if category not in self.expenses["categories"]:
            # Create new category
            self.expenses["categories"][category] = []

        # Add expense to category
        self.expenses["categories"][category].append({
            "date": date,
            "amount": amount,
            "description": description
        })

        # Update monthly summary
        self.update_monthly_summary(date, amount)

        # Save expenses
        self.save_expenses()

    # Update monthly summary
    def update_monthly_summary(self, date, amount):
        # Parse date to get month
        month = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
        # Check if month exists in summary
        if month not in self.expenses["monthly_summary"]:
            # Initialize month summary
            self.expenses["monthly_summary"][month] = 0
        # Add amount to month summary
        self.expenses["monthly_summary"][month] += amount

    # View all expenses
    def view_expenses(self):
        print("Expenses:")
        # Iterate through categories
        for category, expenses in self.expenses["categories"].items():
            print(f"{category}:")
            # Iterate through expenses
            for expense in expenses:
                print(f"  {expense['date']}: {expense['amount']} - {expense['description']}")

    # View monthly summary
    def view_monthly_summary(self):
        print("Monthly Summary:")
        # Iterate through month summaries
        for month, amount in self.expenses["monthly_summary"].items():
            print(f"{month}: {amount}")


# Main function
def main():
    # Create ExpenseTracker instance
    tracker = ExpenseTracker()

    # Loop until exit
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Monthly Summary")
        print("4. Exit")

        # Get user choice
        choice = input("Enter choice: ")

        # Handle user choice
        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.view_monthly_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


# Run main function if script is executed
if __name__ == "__main__":
    main()
