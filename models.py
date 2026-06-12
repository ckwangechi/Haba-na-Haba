class Income:
    def __init__(self, amount, source, date):
        self.amount = amount
        self.source = source
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "source": self.source,
            "date": self.date
        }
    
class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }
    
class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit

    def to_dict(self):
        return {
            "category": self.category,
            "limit": self.limit
        }
    
class Savings:
    def __init__(self, amount, goal, date):
        self.amount = amount
        self.goal = goal
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "goal": self.goal,
            "date": self.date
        }