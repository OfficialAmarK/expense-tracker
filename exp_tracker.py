from datetime import datetime

expenses = []
budget = float(input("Enter your monthly budget (₹): "))

while True:
    print("\n1. Add Expense  2. View Summary  3. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount (₹): "))
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        spent_so_far = sum(e["amount"] for e in expenses)
        remaining = budget - spent_so_far - amount
        expenses.append({"name": name, "amount": amount, "time": current_time, "remaining": remaining})
        print(f"Added: {name} - ₹{amount} (Remaining: ₹{remaining})")
    
    elif choice == "2":
        total = sum(e["amount"] for e in expenses)
        remaining = budget - total
        days = len(set(e["time"][:10] for e in expenses)) or 1
        avg_per_day = total / days
        print(f"\n--- Budget Analysis ---")
        print(f"Budget: ₹{budget} | Spent: ₹{total} | Remaining: ₹{remaining}")
        print(f"Average per day: ₹{avg_per_day:.2f}")
        print(f"Status: {'Over Budget!' if remaining < 0 else 'Within Budget'}\n")
        for e in expenses:
            print(f"{e['time']} | {e['name']}: ₹{e['amount']} | Balance: ₹{e['remaining']}")
    
    elif choice == "3":
        break 