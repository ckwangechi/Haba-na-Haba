import json
import os
from datetime import datetime

data_file = 'data.json'

def load_data():
    if not os.path.exists(data_file):
        data = {
            "income": [],
            "expenses": [],
            "budget": [],
            "savings": []
        }

        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)

        return data

    try:
        with open(data_file, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        data = {
            "income": [],
            "expenses": [],
            "budget": [],
            "savings": []
        }

        save_data(data)
        return data

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def validate_amount(amount):
    return isinstance(amount, (int, float)) and amount >= 0

def format_currency(amount):
    return f"KES {amount:.2f}"

def get_total(records, key="amount"):
    return sum(record.get(key, 0) for record in records)

def search_records(records, field, value):
    return [
        record
        for record in records
        if str(record.get(field, "")).lower() == str(value).lower()
    ]

def print_records(records):
    if not records:
        print("No records found.")
        return

    for index, record in enumerate(records, start=1):
        print(f"{index}. {record}")