from finance_manager import FinanceManager
from utils import format_currency

manager = FinanceManager()

def display_menu():
    print("\nHaba na Haba - Personal Finance Manager")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Set Budget")
    print("4. Add Savings")
    print("5. View Monthly Summary")
    print("6. View All Transactions")
    print("7. Exit")


def add_income_menu():
    try:
        amount = float(input("Enter income amount: "))
        source = input("Enter income source: ")
        manager.add_income(amount, source)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def add_expense_menu():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")
        manager.add_expense(amount, category, description)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def set_budget_menu():
    try:
        category = input("Enter budget category: ")
        limit = float(input("Enter budget limit: "))
        manager.set_budget(category, limit)
    except ValueError:
        print("Invalid input. Please enter a valid number for the limit.")

def add_savings_menu():
    try:
        amount = float(input("Enter savings amount: "))
        goal = input("Enter savings goal: ")
        manager.add_savings(amount, goal)
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def view_monthly_summary_menu():
    summary = manager.get_monthly_summary()
    print(summary)

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
