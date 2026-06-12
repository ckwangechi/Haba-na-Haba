from finance_manager import FinanceManager
from utils import format_currency, save_data, validate_amount

manager = FinanceManager()

# Display menu function
def display_menu():
    print("\nHaba na Haba - Personal Finance Manager")
    print("1. Add Income")
    print("2. Update Income")
    print("3. Delete Income")
    print("4. Add Expense")
    print("5. Update Expense")
    print("6. Delete Expense")
    print("7. Set Budget")
    print("8. Update Budget")
    print("9. Delete Budget")
    print("10. Add Savings")
    print("11. Update Savings")
    print("12. Delete Savings")
    print("13. View Monthly Summary")
    print("14. View All Transactions")
    print("15. Exit")


# Income menu functions
def add_income_menu():
    try:
        amount = float(input("Enter income amount: "))
        source = input("Enter income source: ")
        manager.add_income(amount, source)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def update_income_menu(self, income_id, new_amount, new_source, new_date):
    try:
        new_amount = float(new_amount)
        if validate_amount(new_amount):
            for income in self.data["income"]:
                if income["id"] == income_id:
                    income["amount"] = new_amount
                    income["source"] = new_source
                    income["date"] = new_date
                    save_data(self.data)
                    print("Income updated successfully.")
                    return
                print("Income not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def delete_income(self, income_id):
    for income in self.data["income"]:
        if income["id"] == income_id:
            self.data["income"].remove(income)

            self.save_data()

            print("Income deleted.")
            return

    print("Income not found.")


# Expense menu functions
def add_expense_menu():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")
        manager.add_expense(amount, category, description)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def update_expense_menu(self, expense_id, new_amount, new_category, new_description, new_date):
    try:
        new_amount = float(new_amount)
        if validate_amount(new_amount):
            for expense in self.data["expense"]:
                if expense["id"] == expense_id:
                    expense["amount"] = new_amount
                    expense["category"] = new_category
                    expense["description"] = new_description
                    expense["date"] = new_date
                    save_data(self.data)
                    print("Expense updated successfully.")
                    return
                print("Expense not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def delete_expense(self, expense_id):
    for expense in self.data["expense"]:
        if expense["id"] == expense_id:
            self.data["expense"].remove(expense)

            self.save_data()

            print("Expense deleted.")
            return

    print("Expense not found.")


# Budget menu functions
def set_budget_menu():
    try:
        category = input("Enter budget category: ")
        limit = float(input("Enter budget limit: "))
        date = input("Enter budget date (YYYY-MM-DD): ")
        manager.set_budget(category, limit)
    except ValueError:
        print("Invalid input. Please enter a valid number for the limit.")

def update_budget_menu(self, budget_id, new_amount, new_category, new_limit, new_date):
    try:
        new_amount = float(new_amount)
        if validate_amount(new_amount):
            for budget in self.data["budget"]:
                if budget["id"] == budget_id:
                    budget["amount"] = new_amount
                    budget["category"] = new_category
                    budget["limit"] = new_limit
                    budget["date"] = new_date
                    save_data(self.data)
                    print("Budget updated successfully.")
                    return
                print("Budget not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def delete_budget(self, budget_id):
    for budget in self.data["budget"]:
        if budget["id"] == budget_id:
            self.data["budget"].remove(budget)

            self.save_data()

            print("Budget deleted.")
            return

    print("Budget not found.")


# Savings menu functions
def add_savings_menu():
    try:
        amount = float(input("Enter savings amount: "))
        goal = input("Enter savings goal: ")
        date = input("Enter savings date (YYYY-MM-DD): ")
        manager.add_savings(amount, goal)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def update_savings_menu(self, savings_id, new_amount, new_goal, new_date):
    try:
        new_amount = float(new_amount)
        if validate_amount(new_amount):
            for savings in self.data["savings"]:
                if savings["id"] == savings_id:
                    savings["amount"] = new_amount
                    savings["goal"] = new_goal
                    savings["date"] = new_date
                    save_data(self.data)
                    print("Savings updated successfully.")
                    return
                print("Savings not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def delete_savings(self, savings_id):
    for savings in self.data["savings"]:
        if savings["id"] == savings_id:
            self.data["savings"].remove(savings)

            self.save_data()

            print("Savings deleted.")
            return

    print("Savings not found.")

# Monthly summary menu functions
def view_monthly_summary_menu():
    summary = manager.get_monthly_summary()
    print(summary)


# View all transactions menu functions
def view_all_transactions():
    print("\nAll Income:")
    for income in manager.data['income']:
        print(f"{income['date']}: {format_currency(income['amount'])} from {income['source']}")

    print("\nAll Expenses:")
    for expense in manager.data['expenses']:
        print(f"{expense['date']}: {format_currency(expense['amount'])} for {expense['category']} - {expense['description']}")

    print("\nAll Budgets:")
    for budget in manager.data['budget']:
        print(f"{budget['category']}: {format_currency(budget['limit'])}")

    print("\nAll Savings:")
    for savings in manager.data['savings']:
        print(f"{savings['date']}: {format_currency(savings['amount'])} towards {savings['goal']}")



def main():    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_income_menu()
        elif choice == '2':
            add_expense_menu()
        elif choice == '3':
            set_budget_menu()
        elif choice == '4':
            add_savings_menu()
        elif choice == '5':
            view_monthly_summary_menu()
        elif choice == '6':
            view_all_transactions()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
