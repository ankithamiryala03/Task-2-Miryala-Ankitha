total = 0

while True:
    expense = input("Enter expense (or 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        amount = float(expense)
        total += amount
    except ValueError:
        print("Please enter a valid number.")

print("\nTotal Spent:", total)