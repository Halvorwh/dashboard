import json
import csv
from datetime import datetime
from colorama import Fore

expenses = []

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def format_expense_line(i, expense):
    date_obj = datetime.fromisoformat(expense.get('date', ''))
    formatted_date = date_obj.strftime("%d %b %Y, %H:%M")
    return (f"{i}. Description: {expense['description']:<15}, "
            f"Amount: {expense['amount']:>8.2f}, "
            f"Category: {expense['category']:<10}, "
            f"Date: {formatted_date:<18}")

def add_expense():
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.now()
    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": date.isoformat()
    }
    expenses.append(expense)
    print(Fore.GREEN + "Expense added.")

def view_expenses():
    if not expenses:
        print(Fore.YELLOW + "No expenses yet.")
    else:
        print("=" * 90)
        for i, expense in enumerate(expenses, start=1):
            print(format_expense_line(i, expense))
        print("=" * 90)

def view_total():
    total = sum(expense['amount'] for expense in expenses)
    print(Fore.CYAN + f"Total spent: {total:.2f}")

def edit_expense():
    view_expenses()
    index = int(input("Enter the number of the expense you want to edit: ")) - 1
    if 0 <= index < len(expenses):
        expense = expenses[index]
        new_description = input("Enter new description (or press Enter to keep current): ")
        new_amount = input("Enter new amount (or press Enter to keep current): ")
        new_category = input("Enter new category (or press Enter to keep current): ")
        if new_description:
            expense['description'] = new_description
        if new_amount:
            expense['amount'] = float(new_amount)
        if new_category:
            expense['category'] = new_category
        print(Fore.GREEN + "Expense updated.")
    else:
        print(Fore.RED + "Invalid expense number.")

def delete_expense():
    view_expenses()
    index = int(input("Enter the number of the expense you want to delete: ")) - 1
    if 0 <= index < len(expenses):
        del expenses[index]
        print(Fore.GREEN + "Expense deleted.")
    else:
        print(Fore.RED + "Invalid expense number.")


def run_menu():
    load_expenses()
    while True:
        print("\n--- Expenses ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total spent")
        print("4. Edit expense")
        print("5. Delete expense")
        print("6. Back to main menu")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_expense()
            save_expenses()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            view_total()
        elif choice == 4:
            edit_expense()
            save_expenses()
        elif choice == 5:
            delete_expense()
            save_expenses()
        elif choice == 6:
            break
        else:
            print("Invalid option, try again.")
