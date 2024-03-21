# Function to add an item to the cart
def add_item(cart):
    item = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity: "))
    
    if item in cart:
        cart[item]['quantity'] += quantity
    else:
        cart[item] = {'price': price, 'quantity': quantity}

# Function to remove an item from the cart
def remove_item(cart):
    item = input("Enter the name of the item you want to remove: ")
    if item in cart:
        del cart[item]
    else:
        print("Item not found in cart.")

# Function to view the list of items in the cart
def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, details in cart.items():
            print(f"{item}: Quantity - {details['quantity']}, Price - ${details['price']}")

# Function to calculate total cost of items in the cart
def total_cost(cart):
    total = sum(details['price'] * details['quantity'] for details in cart.values())
    print(f"Total cost: ${total:.2f}")

# Main function to display menu and handle user input
def main():
    cart = {}
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Total cost")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(cart)
        elif choice == '2':
            remove_item(cart)
        elif choice == '3':
            view_cart(cart)
        elif choice == '4':
            total_cost(cart)
        elif choice == '5':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()