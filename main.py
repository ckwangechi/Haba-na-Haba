from finance_manager import FinanceManager
from utils import format_currency, save_data, validate_amount

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print
import questionary




console = Console()

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

def update_income_menu():
    try:
        index = int(input("Income record number: ")) - 1
        amount = float(input("New amount: "))
        source = input("New source: ")
        manager.update_income(index, amount, source)
    except ValueError:
        print("Invalid input.")

def delete_income_menu():
    try:
        index = int(input("Income record number: ")) - 1
        manager.delete_income(index)
    except ValueError:
        print("Invalid input.")


# Expense menu functions
def add_expense_menu():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")
        manager.add_expense(amount, category, description)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def update_expense_menu():
    try:
        index = int(input("Expense record number: ")) - 1
        amount = float(input("New amount: "))
        category = input("New category: ")
        description = input("New description: ")
        manager.update_expense(index, amount, category, description)
    except ValueError:
        print("Invalid input.")

def delete_expense_menu():
    try:
        index = int(input("Expense record number: ")) - 1
        manager.delete_expense(index)
    except ValueError:
        print("Invalid input.")


# Budget menu functions
def set_budget_menu():
    try:
        category = input("Enter budget category: ")
        limit = float(input("Enter budget limit: "))
        date = input("Enter budget date (YYYY-MM-DD): ")
        manager.set_budget(category, limit)
    except ValueError:
        print("Invalid input. Please enter a valid number for the limit.")

def update_budget_menu():
    try:
        index = int(input("Budget record number: ")) - 1
        category = input("Category: ")
        limit = float(input("New limit: "))
        manager.update_budget(index, category, limit)
    except ValueError:
        print("Invalid input.")

def delete_budget_menu():
    try:
        index = int(input("Budget record number: ")) - 1
        manager.delete_budget(index)
    except ValueError:
        print("Invalid input.")


# Savings menu functions
def add_savings_menu():
    try:
        amount = float(input("Enter savings amount: "))
        category = input("Enter savings category: ")
        goal = input("Enter savings goal: ")
        date = input("Enter savings date (YYYY-MM-DD): ")
        manager.add_savings(amount, category, goal, date)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def update_savings_menu():
    try:
        index = int(input("Savings record number: ")) - 1
        amount = float(input("New amount: "))
        goal = input("New goal: ")
        manager.update_savings(index, amount, goal)
    except ValueError:
        print("Invalid input.")

def delete_savings_menu():
    try:
        index = int(input("Savings record number: ")) - 1
        manager.delete_savings(index)
    except ValueError:
        print("Invalid input.")


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

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_income_menu()
        elif choice == "2":
            update_income_menu()
        elif choice == "3":
            delete_income_menu()
        elif choice == "4":
            add_expense_menu()
        elif choice == "5":
            update_expense_menu()
        elif choice == "6":
            delete_expense_menu()
        elif choice == "7":
            set_budget_menu()
        elif choice == "8":
            update_budget_menu()
        elif choice == "9":
            delete_budget_menu()
        elif choice == "10":
            add_savings_menu()
        elif choice == "11":
            update_savings_menu()
        elif choice == "12":
            delete_savings_menu()
        elif choice == "13":
            view_monthly_summary_menu()
        elif choice == "14":
            view_all_transactions()
        elif choice == "15":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
