# 7 - 9 - 2026

# Predifined restraunt menu
menu = {
    "Burger": 5,
    "Pizza": 8,
    "Pasta": 7,
    "Salad": 4,
    "Soda": 2
}

print("Welcome the the Restraunt!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: ${price}")

# Ask how many items to order
n = int(input("\nHow many items would you like to order? "))

total = 0
for i in range(n):
    order = input(f"Enter item {i+1}:")
    if order in menu:
        total += menu[order]
        print(f"Added {order} - ${menu[order]}")
    else:
        print(f"Sorry, {order} is not on the menu.")

print(f"\nYour total bill is: ${total}")