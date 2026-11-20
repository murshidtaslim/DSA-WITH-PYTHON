expenses = [120,50,300,80,200,50,450]

while True:
    print(f"\n=== Expense Analyzer ===")
    print(f"1. Show all expenses")
    print(f"2. Add new expense")
    print(f"3. Total and Heighet expense")
    print(f"4. Search and expense")
    print(f"5. Reverse history")
    print(f"6. Max-3 day expenses")
    print(f"7. Sort expenses Low to high")
    print(f"8. Exit")

    choice = (input("Enter Your Choice: "))
    if choice == "1":
        print(f"\nExpenses List: {expenses}\n")
    elif choice == "2":
        amount=int(input("Enter Amount: "))
        expenses.append(amount)
        print(f"\nYour Updated! Expenses: {expenses}\n")
    elif choice == "3":
        print(f"\nYour Total expense is RS{sum(expenses)}, and Heighest expense is RS{max(expenses)}\n")
    elif choice == "4":
        day_indx = int(input("\nEnter day number: "))
        if day_indx <= len(expenses-1):
            print(f"\nYour Expense is RS{expenses[day_indx]}\n")
        else:
            print("\nExpense not found!\n")
    elif choice == "5":
        #expenses.reverse()
        print(f"\nReversed List: {expenses[::-1]}\n")
    elif choice == "6":
        #expenses.sort(reverse=True)
        print(f"\nMax-3 Day's Expenses: {sorted(expenses,reverse=True)[:3]}\n")
    elif choice == "7":
        #expenses.sort()
        print(f"\nYour Low-High Expenses: {sorted(expenses)}\n")
    elif choice == "8":
        print("\nProgramme Closed!\n")
        break
    else:
        print("\nWrong Choice!\n")
