# expense tracker that keeps track of individual expenses
# per category and computes total expenses

# refactoring using list of dictionaries to store events, for 
# more detailed expense tracking/flexibility

expenses = []

def add_expense(expenses, category: str, amount: float):
    expenses.append({"category": category, "amount": amount}) # create dict for each expense

# function to compute total expenses per category
def totals_per_category(expenses):
    totals = {}
    for e in expenses:
        category = e.get("category")
        amount = e.get("amount", 0.0)
        totals[category] = totals.get(category, 0.0) + amount
    return totals

# function to print summary of expenses per category
def print_summary(expenses) -> float:
    total = 0.0
    totals = totals_per_category(expenses) # dict to store total expenses per category
    
    # print summary of expenses per category
    for category, amount in totals.items():
        print(f"Category: {category} | Total Amount: ${amount:.2f}")
        total += amount
    print(f"Total Expenses: ${total:.2f}")
    return total

add_expense(expenses, "food", 25.24)
add_expense(expenses, "transportation", 15.00)
add_expense(expenses, "entertainment", 40.00)
add_expense(expenses, "food", 30.50)
print_summary(expenses)
