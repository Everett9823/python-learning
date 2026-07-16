expenses = []

def add_expense(): # Creates a function to add an expense
    name = input("Enter the name of the expense: ")
    price = float(input("Enter the price of the expense: "))
    categories = ["Food", "Transportation", "Entertainment", "Utilities", "Housing", "Other"]
    
    category = input("Enter what type of expense it is: ")

    if category not in categories:
        print("Invalid category. Please choose from: Food, Transportation, Entertainment, Utilities, Housing, Other.")
        return None


    expense = {
        "name": name,
        "price": price,
        "category": category
    }

    return expense


while True:
    expense = add_expense()      # call the function
    expenses.append(expense)     # add the returned dictionary to the list

    choice = input("Do you want to add another expense (yes/no): ").lower()

    if choice == "no":
        break
    elif choice != "yes": # No choice already adressed
        print("Invalid input.")

print("Here is your summary:")

for expense in expenses:
    print(
        expense["name"],
        "- $",
        expense["price"],
        "-",
        expense["category"]
    )


    

 
       




