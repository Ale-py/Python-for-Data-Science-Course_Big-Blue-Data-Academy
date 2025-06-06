expenses ={
    "hotels" : [],
    "transportation" : [],
    "food" : []
}

while True:
    category = input("Please enter expense category or DONE to finish: ")
    print(category)
    if category == "DONE":
        break
    elif category in expenses:
        amount = float(input("Please provide the amount in eyros: "))
        expenses[category].append(amount)
    else:
        print("Invalid Category. Please provide a valid category (hotels, transportation ,food)")

total_expenses = 0

for category, amounts in expenses.items():
    category_total = sum(amounts)
    print(f"For category {category} , total expenses are : {category_total} euros")
    total_expenses = total_expenses + category_total
print(f"Total expenses are {total_expenses} euros")

















