from collections import defaultdict

def get_user_input():
    """
    Collects user input for amount, description, and category.
    Handles invalid amount inputs gracefully.
    """
    while True:
        try:
            amount = float(input("Enter the amount spent: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    
    date = input("Enter the date (YYYY-MM-DD): ")
    
    return amount, description, category, date

def monthly_summary(expenses):
    """
    Returns a summary of expenses by month.
    
    Parameters:
    - expenses: List of expense dictionaries
    
    Returns:
    - Dictionary with months as keys and total expenses as values
    """
    summary = defaultdict(float)
    for expense in expenses:
        month = expense["date"][:7]  # Assuming date is stored as "YYYY-MM-DD"
        summary[month] += expense["amount"]
    return summary

def category_summary(expenses):
    """
    Returns a summary of expenses by category.
    
    Parameters:
    - expenses: List of expense dictionaries
    
    Returns:
    - Dictionary with categories as keys and total expenses as values
    """
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense["category"]] += expense["amount"]
    return summary

def main():
    """
    Main function to run the expense tracker.
    Provides a simple CLI for user interaction.
    """
    expenses = []

    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View monthly summary")
        print("3. View category summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount, description, category, date = get_user_input()
            expense = {
                "amount": amount,
                "description": description,
                "category": category,
                "date": date
            }
            expenses.append(expense)

        elif choice == "2":
            print("Monthly Summary")
            for month, total in monthly_summary(expenses).items():
                print(f"{month}: ${total:.2f}")

        elif choice == "3":
            print("Category Summary")
            for category, total in category_summary(expenses).items():
                print(f"{category}: ${total:.2f}")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
