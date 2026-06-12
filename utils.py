import json
from datetime import datetime

def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

            if not data:
                data = {
                    "income": [],
                    "expenses": [],
                    "budget": [],
                    "savings": []
                }
            return data
    except FileNotFoundError:
        data = {
            "income": [],
            "expenses": [],
            "budget": [],
            "savings": []
        }

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def validate_amount(amount):
    return isinstance(amount, (int, float)) and amount >= 0

def format_currency(amount):
    return f"KES {amount:.2f}"