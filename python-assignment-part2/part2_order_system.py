menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

#Task 1 — Explore the Menu

categories = ["Starters", "Mains", "Desserts"]

# Loop through our specified categories first
for category in categories:
    print(f"\n===== {category} =====")
    
    #find items matching the current category
    for item_name, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            status = "Available" if details["available"] else "Unavailable"
            
            print(f"{item_name:<15} ₹{price:>6.2f}   [{status}]")


total_items = len(menu)
print("Total number of items on the menu", total_items)

available_items = sum(1 for item in menu.values() if item["available"])
print("Total number of available items:", available_items)

most_expensive_item = max(menu.items(), key=lambda x: x[1]["price"])
print("The most expensive item (name + price):", most_expensive_item[0], "₹", most_expensive_item[1]["price"])

print("\nAll items priced under ₹150 (name + price):")
for name, details in menu.items():
    if details["price"] < 150:
        print(name, "₹", details["price"])

#Task 2 — Cart Operations

cart = []

def add_to_cart(item_name, quantity):

    if item_name not in menu:
        print(f"{item_name} is not on the menu.")
        return

    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable.")
        return

    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return
    
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    
    print(f"Added {item_name} x{quantity} to cart")

def remove_from_cart(item_name):
    
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"{item_name} removed from cart.")
            return
    
    print(f"{item_name} is not in the cart.")

def update_quantity(item_name, new_quantity):
    
    for item in cart:
        if item["item"] == item_name:

            if new_quantity <= 0:
                cart.remove(item)
                print(f"{item_name} removed from cart (quantity set to 0).")
            else:
                item["quantity"] = new_quantity
                print(f"{item_name} quantity updated to {new_quantity}")
            
            return

    print(f"{item_name} is not in the cart.")

add_to_cart("Paneer Tikka", 2)

add_to_cart("Gulab Jamun", 1)

add_to_cart("Paneer Tikka", 1)

add_to_cart("Mystery Burger", 1)

add_to_cart("Chicken Wings", 1)

remove_from_cart("Gulab Jamun")

def generate_bill():
    print("\n========== Order Summary ==========")
    
    subtotal = 0
    
    for item in cart:
        name = item["item"]
        quantity = item["quantity"]
        price = item["price"]
        total_price = quantity * price
        
        subtotal += total_price
        
        print(f"{name:<18} x{quantity:<5} ₹{total_price:>7.2f}")
    
    print("------------------------------------")
    
    gst = subtotal * 0.05
    total = subtotal + gst
    
    print(f"{'Subtotal:':<25} ₹{subtotal:>7.2f}")
    print(f"{'GST (5%):':<25} ₹{gst:>7.2f}")
    print(f"{'Total Payable:':<25} ₹{total:>7.2f}")
    
    print("====================================")

generate_bill()

#Task 3 — Inventory Tracker with Deep Copy

import copy

inventory_backup = copy.deepcopy(inventory)

print("Before making any changes:")
print("Inventory:", inventory)
print("Inventory Backup:", inventory_backup)

inventory["Paneer Tikka"]["stock"] = 20

print("\nAfter changing original inventory stock:")
print("Inventory:", inventory)
print("Inventory Backup:", inventory_backup)

inventory = copy.deepcopy(inventory_backup)

print("\nAfter restoring inventory to original state:")
print("Inventory:", inventory)
print("Inventory Backup:", inventory_backup)

for cart_item in cart:
    item_name = cart_item["item"]
    quantity_needed = cart_item["quantity"]

    if item_name in inventory:
        available_stock = inventory[item_name]["stock"]

        if available_stock >= quantity_needed:
            inventory[item_name]["stock"] -= quantity_needed
            print(f"\nFulfilled {quantity_needed} unit(s) of {item_name}.")
        else:
            print(f"\nWarning: Insufficient stock for {item_name}.")
            print(f"Only {available_stock} unit(s) available. Deducting available stock.")
            inventory[item_name]["stock"] = 0

print("\nReorder Alerts:")
for item_name, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {item_name} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

print("\nFinal Inventory:")
print(inventory)

print("\nInventory Backup:")
print(inventory_backup)

#Task 4 — Daily Sales Log Analysis

print("\nRevenue Per Day:")
daily_revenue = {}

for date, orders in sales_log.items():
    total_revenue = sum(order["total"] for order in orders)
    daily_revenue[date] = total_revenue
    print(f"{date}: ₹{total_revenue:.2f}")

best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nBest-selling day: {best_day} — ₹{daily_revenue[best_day]:.2f}")

item_order_count = {}

for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:
            if item not in item_order_count:
                item_order_count[item] = 0
            item_order_count[item] += 1

most_ordered_item = max(item_order_count, key=item_order_count.get)
print(f"\nMost ordered item: {most_ordered_item} — appeared in {item_order_count[most_ordered_item]} orders")

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue Per Day:")
daily_revenue = {}

for date, orders in sales_log.items():
    total_revenue = sum(order["total"] for order in orders)
    daily_revenue[date] = total_revenue
    print(f"{date}: ₹{total_revenue:.2f}")

best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nUpdated best-selling day: {best_day} — ₹{daily_revenue[best_day]:.2f}")

print("\nAll Orders:")
all_orders = []

for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))

for index, (date, order) in enumerate(all_orders, start=1):
    items_text = ", ".join(order["items"])
    print(f"{index}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_text}")
