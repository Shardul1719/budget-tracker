import csv
import os

FILENAME = 'data.csv'

# Initialize CSV
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Type", "Amount", "Category", "Note"])

def generate_id():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        return len(rows)

def add_transaction():
    t_type = input("Type (Income/Expense): ").capitalize()
    amount = float(input("Amount: "))
    category = input("Category (e.g. Food, Rent, Salary): ")
    note = input("Note: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([generate_id(), t_type, amount, category, note])
    print("Transaction added!\n")

def view_summary():
    income = 0
    expense = 0
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Type"] == "Income":
                income += float(row["Amount"])
            elif row["Type"] == "Expense":
                expense += float(row["Amount"])
    print(f"\nTotal Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Balance: ₹{income - expense}\n")

def view_transactions():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

def delete_transaction():
    tid = input("Enter Transaction ID to delete: ")
    rows = []
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[0] != tid]

    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Transaction deleted!\n")

def menu():
    while True:
        print("== Budget Tracker ==")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View All Transactions")
        print("4. Delete Transaction")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
