from models import Customer, MenuItem, Menu, Order

# Test 1: Order total with multiple items
def test_calculate_total_with_multiple_items():
    order = Order()
    order.add_item(MenuItem("Spicy Burger", 9.99, "Food", 4.5))
    order.add_item(MenuItem("Large Soda", 2.99, "Drinks", 4.0))
    assert order.compute_total() == 12.98

# Test 2: Empty order total should be zero
def test_order_total_is_zero_when_empty():
    order = Order()
    assert order.compute_total() == 0

# Test 3: Filter menu items by category
def test_filter_by_category():
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 9.99, "Food", 4.5))
    menu.add_item(MenuItem("Large Soda", 2.99, "Drinks", 4.0))
    menu.add_item(MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8))
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 1
    assert drinks[0].name == "Large Soda"