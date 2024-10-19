import argparse
import json
from datetime import datetime
import os

# File to store expense data
DATA_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(description, amount):
    expenses = load_expenses()
    expense = {
        "id": len(expenses) + 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense['id']})")

def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        print("ID  Date       Description  Amount")
        for exp in expenses:
            print(f"{exp['id']}   {exp['date']}  {exp['description']}  ${exp['amount']}")

def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [exp for exp in expenses if exp['id'] != expense_id]
    save_expenses(expenses)
    print(f"Expense deleted successfully")

def summary(month=None):
    expenses = load_expenses()
    if month:
        expenses = [exp for exp in expenses if datetime.strptime(exp['date'], '%Y-%m-%d').month == month]
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total expenses: ${total}")

# CLI parser
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the expense')

    list_parser = subparsers.add_parser('list', help='List all expenses')

    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', type=int, required=True, help='ID of the expense to delete')

    summary_parser = subparsers.add_parser('summary', help='Summary of expenses')
    summary_parser.add_argument('--month', type=int, help='Summary of expenses for a specific month')

    args = parser.parse_args()

    if args.command == 'add':
        add_expense(args.description, args.amount)
    elif args.command == 'list':
        list_expenses()
    elif args.command == 'delete':
        delete_expense(args.id)
    elif args.command == 'summary':
        if args.month:
            summary(args.month)
        else:
            summary()

if __name__ == '__main__':
    main()
