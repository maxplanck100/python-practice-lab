class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})

    def total_expenses(self):
        return sum(exp["amount"] for exp in self.expenses)
