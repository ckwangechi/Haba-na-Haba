from models import Income, Expense, Budget, Savings
from utils import (load_data, save_data, get_current_date, validate_amount, format_currency)

from rich.console import Console
console = Console()

class FinanceManager:
    def __init__(self):
        self.file_path = 'data.json'
        self.data = load_data()

# Income functions
    def add_income(self, amount, source):
        if validate_amount(amount):
            income = Income(amount, source, get_current_date())
            self.data['income'].append(income.to_dict())
            save_data(self.data)
            console.print("Income added successfully.")
        else:
            console.print("Invalid amount. Please enter a positive number.")

    def update_income(self, index, amount, source):
        if index < 0 or index >= len(self.data["income"]):
            console.print("Invalid income record.")
            return

        if validate_amount(amount):
            self.data["income"][index]["amount"] = amount
            self.data["income"][index]["source"] = source
            save_data(self.data)
            console.print("Income updated successfully.")

    def delete_income(self, index):
        if index < 0 or index >= len(self.data["income"]):
            console.print("Invalid income record.")
            return

        self.data["income"].pop(index)
        save_data(self.data)
        console.print("Income deleted successfully.")

# Expense functions
    def add_expense(self, amount, category, description):
        if validate_amount(amount):
            expense = Expense(amount, category, description, get_current_date())
            self.data['expenses'].append(expense.to_dict())
            save_data(self.data)
            console.print("Expense added successfully.")
        else:
            console.print("Invalid amount. Please enter a positive number.")

    def update_expense(self, index, amount, category, description):
        if index < 0 or index >= len(self.data["expenses"]):
            console.print("Invalid expense record.")
            return

        if validate_amount(amount):
            self.data["expenses"][index]["amount"] = amount
            self.data["expenses"][index]["category"] = category
            self.data["expenses"][index]["description"] = description
            save_data(self.data)
            console.print("Expense updated successfully.")

    def delete_expense(self, index):
        if index < 0 or index >= len(self.data["expenses"]):
            console.print("Invalid expense record.")
            return

        self.data["expenses"].pop(index)
        save_data(self.data)
        console.print("Expense deleted successfully.")

# Budget functions
    def set_budget(self, category, limit):
        if not validate_amount(limit):
            print("Invalid budget.")
            return

        budget = Budget(category, limit)
        self.data["budget"].append(budget.to_dict())
        save_data(self.data)
        console.print("Budget added successfully.")

    def update_budget(self, index, category, limit):
        if index < 0 or index >= len(self.data["budget"]):
            console.print("Invalid budget record.")
            return

        if validate_amount(limit):
            self.data["budget"][index]["category"] = category
            self.data["budget"][index]["limit"] = limit
            save_data(self.data)
            console.print("Budget updated successfully.")

    def delete_budget(self, index):
        if index < 0 or index >= len(self.data["budget"]):
            print("Invalid budget record.")
            return

        self.data["budget"].pop(index)
        save_data(self.data)
        console.print("Budget deleted successfully.")

# Savings functions
    def add_savings(self, amount, goal, date=None):
        if not validate_amount(amount):
            console.print("Invalid amount.")
            return

        if date is None:
            date = get_current_date()

        savings = Savings(amount, goal, date)
        self.data["savings"].append(savings.to_dict())
        save_data(self.data)
        console.print("Savings added successfully.")

    def update_savings(self, index, amount, goal):
        if index < 0 or index >= len(self.data["savings"]):
            console.print("Invalid savings record.")
            return

        if validate_amount(amount):
            self.data["savings"][index]["amount"] = amount
            self.data["savings"][index]["goal"] = goal
            save_data(self.data)
            console.print("Savings updated successfully.")

    def delete_savings(self, index):
        if index < 0 or index >= len(self.data["savings"]):
            console.print("Invalid savings record.")
            return

        self.data["savings"].pop(index)
        save_data(self.data)
        console.print("Savings deleted successfully.")

# Totals, categories and  summaries functions
    def get_total_income(self):
        return sum(income['amount'] for income in self.data['income'])
    def get_category_income(self, category):
        return [income for income in self.data['income'] if income['source'] == category]   
    
    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.data['expenses'])
    def get_category_expenses(self, category):
        return [expense for expense in self.data['expenses'] if expense['category'] == category]
    
    def get_total_budget(self):
        return sum(budget['limit'] for budget in self.data['budget'])
    def get_category_budget(self, category):
        return [budget for budget in self.data['budget'] if budget['category'] == category]
    
    def get_total_savings(self):
        return sum(savings['amount'] for savings in self.data['savings'])
    def get_category_savings(self, goal):
        return [savings for savings in self.data['savings'] if savings['goal'] == goal]
    

# Report generation functions
    def get_monthly_summary(self):
        total_income = self.get_total_income()
        total_expenses = self.get_total_expenses()
        total_budget = self.get_total_budget()
        total_savings = self.get_total_savings()
        balance = self.get_balance()

        summary = f"Monthly Summary:\nTotal Income: {format_currency(total_income)}\nTotal Expenses: {format_currency(total_expenses)}\nTotal Budget: {format_currency(total_budget)}\nTotal Savings: {format_currency(total_savings)}\nBalance: {format_currency(balance)}"
        return summary

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()
    
    def get_budget_status(self, category):
        category_expenses = self.get_category_expenses(category)
        category_budget = self.get_category_budget(category)
        if category_budget:
            budget_limit = category_budget[0]['limit']
            total_expenses = sum(expense['amount'] for expense in category_expenses)
            if total_expenses > budget_limit:
                return f"Over budget by {format_currency(total_expenses - budget_limit)}"
            else:
                return f"Within budget. Remaining: {format_currency(budget_limit - total_expenses)}"
        else:
            return "No budget set for this category."
        
    def view_all_transactions(self):
        return {
            "income": self.data['income'],
            "expenses": self.data['expenses'],
            "budget": self.data['budget'],
            "savings": self.data['savings']
        }