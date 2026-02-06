# Expense Tracker
# A simple progam to track expenses by category and compute totals.

# consider lesson 2:
# what do i need to store? 
# does order matter? uniqueness? meaning associated to value?
# order? no bc computing totals
# uniqueness? no bc somme expenses can be same amount
# meaning associated to value? yes, values to sum up with each 
# other depend on which category each value is associated with

# thus, dictionary is optimat data structure

expenses = {}
expenses_list = []

# what type of expenses are we adding? what do these expenses look like?
# persona: college student living alone on campus
# categories: food, transportation, entertainment, education, others
# how specific do we want to get with each category?
# say this student just wants to track total amount across each category. 
    # not interested in where each expense occurred. 

# we want to add many expenses, so write a function
def add_expense(expenses, category: str, amount: float):
    if category in expenses: # if category already exists
        expenses[category] += amount
    else:
        expenses[category] = amount  # initialize: if the key is found in the dict:

    #print(f"Added expense: {amount} to category: {category}") 

# function to compute total expenses
def print_summary(expenses) -> float:
    total = 0.0
    for category, amount in expenses.items(): # See A*
        total += amount
        print(f"Category: {category} | Amount: ${amount:.2f}")
    print(f"Total Expenses: ${total}")
    return total

add_expense(expenses, "food", 25.24)
add_expense(expenses, "transportation", 15.00)
add_expense(expenses, "entertainment", 40.00)
add_expense(expenses, "food", 30.50)        
print_summary(expenses)
# A*: wouldn't it be more efficient to have all the values added up instead of iterating twice?