# expense tracker that keeps track of individual expenses
# per category and computes total expenses

# refactoring using list of dictionaries to store events, for 
# more detailed expense tracking/flexibility

expenses = []

def add_expense(expenses, category: str, amount: float):
    expenses.append({"category": category, "amount": amount}) # create dict for each expense
    
