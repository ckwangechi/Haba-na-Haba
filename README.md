# Haba na Haba CLI - Personal Finance Tracker

## Overview

Haba na Haba CLI is a command-line personal finance management application built with Python. The application helps users track income, monitor expenses, manage category budgets, and generate monthly financial summaries.

The name "Haba na Haba" stems from the Swahili methali "Haba na haba hujaza kibaba" which reflects the idea that small, consistent financial decisions can lead to better money management over time.

---

## Problem Statement

Many individuals struggle to keep track of their income and expenses, making it difficult to understand spending habits and maintain financial discipline.

Haba na Haba CLI provides a simple solution by allowing users to record transactions, set spending limits, and monitor their financial progress directly from the command line.

---

## Features

### Income Management

* Add, update and delete income transactions
* Record income source
* Automatically save income records

### Expense Management

* Add, update and delete expense transactions
* Categorize expenses
* Track spending by category

### Budget Management

* Set category-specific budgets
* Monitor spending against budgets
* Receive warnings when budgets are exceeded

### Savings Tracker

* Set savings goals
* Track Savings

### Financial Reporting

* View monthly income totals
* View monthly expense totals
* Calculate remaining balance
* Display spending breakdown by category

### Data Persistence

* Save data to JSON
* Load data automatically when the application starts

---

## Technologies Used

* Python 3
* JSON
* Object-Oriented Programming (OOP)
* Command Line Interface (CLI)
* Rich
* Questionary

---

## Project Structure

haba-na-haba/

├── main.py              # Main application and menu

├── finance_manager.py   # Business logic

├── models.py            # Data models

├── utils.py             # Helper functions

├── data.json            # Stores financial records

├── requirements.txt

├── README.md

└── .gitignore

---

## System Architecture

main.py   

↓ calls

finance_manager.py

↓ uses

models.py

↓ uses

utils.py

↓ reads/writes

data.json

---

## Modules

main.py
- Handles the user interface, menu navigation, and user input.

finance_manager.py
Contains all business logic for:
- Income management
- Expense management
- Budget management
- Savings management
- Financial summaries

models.py

Defines the following classes:
- Income
- Expense
- Budget
- Savings

utils.py
Provides helper functions including:
- Loading and saving data
- Currency formatting
- Date handling
- Amount validation
- Record searching
- Total calculations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ckwangechi/Haba-na-Haba.git
```

2. Navigate into the project folder:
```bash
cd haba-na-haba
```

3. Install the required packages:
```bash
pip install -r requirements.txt

```

4. Run the application:
```bash
python main.py
```
---

## Menu Options

1. Add Income
2. Update Income
3. Delete Income
4. Add Expense
5. Update Expense
6. Delete Expense
7. Set Budget
8. Update Budget
9. Delete Budget
10. Add Savings
11. Update Savings
12. Delete Savings
13. View Monthly Summary
14. View All Transactions
15. Exit

---

## Object-Oriented Design

The project uses three main classes:

### Income

Stores:

* Amount
* Source
* Date

### Expense

Stores:

* Amount
* Category
* Description
* Date

### Budget

Stores:

* Category
* Spending Limit

### Savings

Stores:

* Amount
* Savings goal 
* Date

---

## Future Improvements

* Export reports to CSV
* Monthly trend analysis
* Data visualization
* Authentication system
* Multi-user support

---

## Author

Christine Wangechi Karuga

## License

MIT License