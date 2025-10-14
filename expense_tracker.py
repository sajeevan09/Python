import csv
from datetime import datetime
import os  

FOLDER_NAME = os.path.expanduser("~/Documents/ExpenseTracker")
FILE_NAME = os.path.join(FOLDER_NAME, "expenses.csv")

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Note"])  # headers

def add_expense():
    """Add a new expense to the CSV file with input validation."""
    
    #Date input
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press enter for today: ")
        if date_input.strip() == "":
            date = datetime.today().strftime("%Y-%m-%d")
            break
        else:
            try:
                datetime.strptime(date_input, "%Y-%m-%d")
                date = date_input
                break
            except ValueError:
                print(" Invalid date format. Using today’s date instead.")
                #date = datetime.today().strftime("%Y-%m-%d")

    #Category input
    while True:
        category = input("Enter category (e.g., Food, Travel, Rent): ").strip()
        if category:
            break
        print(" Category cannot be empty.")

    #Amount input
    while True:
        amount_input = input("Enter amount spent: ").strip()
        try:
            amount = float(amount_input)
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print(" Please enter a valid positive number.")

    # Note input
    note = input("Enter a short note (optional): ").strip()

    # Save to CSV
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print(" Expense added successfully!\n")

def view_expenses():
    """Display all recorded expenses."""
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            print("\n" + "\t".join(headers))
            print("-" * 50)
            for row in reader:
                print("\t".join([str(cell) for cell in row]))
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

def summarize_expenses():
    """Show total and per-category spending."""
    totals = {}
    total_spent = 0.0

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                try:
                    amount = float(row[2].strip())
                except (ValueError, IndexError):
                    continue  # skip bad rows
                category = row[1].strip()
                total_spent += amount
                totals[category] = totals.get(category, 0) + amount
    except FileNotFoundError:
        print("No expenses recorded yet.\n")
        return

    print("\n Expense Summary ")
    print("-" * 30)
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
    print(f"\nTotal Spent: ${total_spent:.2f}\n")

def delete_expense():
    """Delete an expense by row number."""
    try:
        with open(FILE_NAME, "r") as file:
            rows = list(csv.reader(file))

        if len(rows) <= 1:
            print("No expenses to delete.\n")
            return

        # Show all expenses with numbers
        print("\nExpenses:")
        for i, row in enumerate(rows[1:], start=1):
            print(f"{i}. {row[0]} | {row[1]} | {row[2]} | {row[3]}")

        while True:
            choice = input("Enter the number of the expense to delete: ").strip()
            try:
                index = int(choice)
                if 1 <= index < len(rows):
                    break
                else:
                    print("Number out of range. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

        # Remove the chosen row
        del rows[index]

        # Save the CSV again
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(" Expense deleted\n")
    except Exception as e:
        print("Error:", e)

def main():
    """Main menu for the expense tracker."""
    print("=== Expense Tracker ===")

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print(" Invalid choice. Enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
