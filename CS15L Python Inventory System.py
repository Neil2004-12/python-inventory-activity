item_names = []  
item_prices = {} 
def display_menu():
    
    print("Inventory System:")
    print("___________________________")
    print("(1) Add Item")
    print("(2) Update Price")
    print("(3) Exit")
    print("___________________________")

def add_item():
    """Add new item"""
    print("\nAdd Item:")
    print("___________________________")
    item_name = input("Enter item name: ").strip().capitalize()

    if item_name in item_names:
        print(f"Error: Item '{item_name}' already exists in the inventory list.")
        return

    try:
        item_price = float(input("Enter price: "))
        if item_price < 0:
             print("Error: Price cannot be negative.")
             return
    except ValueError:
        print("Error: Invalid price entered. Please enter a number.")
        return

    item_names.append(item_name)
    item_prices[item_name] = item_price
    print("Item added successfully!")

def update_price():
    """Updates the price of the item."""
    print("\nUpdate Price")
    print("___________________________")
    item_name = input("Enter item name to update: ").strip().capitalize()

    if item_name in item_prices:
        try:
            new_price = float(input("Enter new price: "))
            if new_price < 0:
                 print("Error: New price cannot be negative.")
                 return
            
            item_prices[item_name] = new_price
            print("Price updated successfully!")
        except ValueError:
            print("Error: Invalid price entered. Please enter a number.")
    else:
        print(f"Item '{item_name}' not found in the inventory.")

while True:
    display_menu()
    choice = input("Choice: ").strip()

    if choice == '1':
        add_item()
    elif choice == '2':
        update_price()
    elif choice == '3':
        print("\nExiting system...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
