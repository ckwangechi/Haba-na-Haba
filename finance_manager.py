from models import Income, Expense, Budget, Savings
from utils import (load_data, save_data, get_current_date, validate_amount, format_currency)

class FinanceManager:
    def __init__(self):
        self.file_path = 'data.json'
        self.data = load_data()

    def add_income(self, amount, source):
        if validate_amount(amount):
            income = Income(amount, source, get_current_date())
            self.data['income'].append(income.to_dict())
            save_data(self.data)
            print("Income added successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def add_expense(self, amount, category, description):
        if validate_amount(amount):
            expense = Expense(amount, category, description, get_current_date())
            self.data['expenses'].append(expense.to_dict())
            save_data(self.data)
            print("Expense added successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def set_budget(self, category, limit):
        if validate_amount(limit):
            budget = Budget(category, limit)
            self.data['budget'].append(budget.to_dict())
            save_data(self.data)
            print("Budget set successfully.")
        else:
            print("Invalid limit. Please enter a positive number.")

    def add_savings(self, amount, goal):
        if validate_amount(amount):
            savings = Savings(amount, goal, get_current_date())
            self.data['savings'].append(savings.to_dict())
            save_data(self.data)
            print("Savings added successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")


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