from expense import Expense
import calendar
import datetime

def main():
    print("Running Expense Tracker📊")
    expense_file_path = "myexpense.csv"
    budget = 2000

    #take  expense from the user
    expense = get_the_user_expense()
    
    #Add the expense to a file
    save_expense_to_File(expense, expense_file_path)

    #Read the file and Summarise it
    summarize_the_file(expense_file_path,budget)
    

def get_the_user_expense():
    print("Taking the user expense....")
    expense_name = input("Please enter the expense name: ")
    expense_amount = float(input("Please enter the expense amount: "))
    

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Please select the category")
        for i,category in enumerate(expense_categories):
            print(f"{i+1}.{category}")
        
        valid_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter the category number {valid_range}: "))-1
        selected_category = expense_categories[selected_index]

        if selected_index in range(len(expense_categories)):
            new_expense = Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. please try again")
        

def save_expense_to_File(expense: Expense,expense_file_path):
    print(f"User {expense} saved to {expense_file_path}")
    with open(expense_file_path,'a',encoding="utf-8")as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_the_file(expense_file_path,budget):
    print("User expense summarised")
    expenses:list[Expense] = []
    with open(expense_file_path,'r',encoding="utf-8")as f:
        lines = f.readlines()
        for line in lines:
            
            expense_name,expense_amount,expense_category = line.strip().split(',')
            line_expense = Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}

    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    
    
    print("Expense by category📈")
    for key,amount in amount_by_category.items():
        print(f"{key} : ${amount:.2f}")
    
    total_spent = sum([x.amount for x in expenses])

    print(f"💵Total Spent: ${total_spent:.2f}")
    remaining_budget = budget - total_spent
    print(f"✅Budget left: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    budget_per_day = remaining_budget/remaining_days
    print(green(f"👉Budget per day: ${budget_per_day:2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"




if __name__=='__main__':
    main()