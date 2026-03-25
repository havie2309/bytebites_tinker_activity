from models import Customer, MenuItem, Menu, Order

# Create some menu items
burger = MenuItem("Spicy Burger", 9.99, "Food", 4.5)
soda = MenuItem("Large Soda", 2.99, "Drinks", 4.0)
cake = MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8)

# Test Menu
menu = Menu()
menu.add_item(burger)
menu.add_item(soda)
menu.add_item(cake)

print("All items:", [item.name for item in menu.items])
print("Drinks only:", [item.name for item in menu.filter_by_category("Drinks")])

# Test Order
order = Order()
order.add_item(burger)
order.add_item(soda)
print("Order total:", order.compute_total())

# Test Customer
customer = Customer("Vy")
customer.add_to_purchase_history(order)
print("Customer:", customer.name)
print("Purchase history count:", len(customer.purchase_history))