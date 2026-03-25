# ByteBites - Core Models
# Four classes:
# - Customer: tracks name and purchase history
# - MenuItem: represents a food item with name, price, category, and popularity rating
# - Menu: holds all menu items and supports filtering by category
# - Order: groups selected items and computes the total cost

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []
    
    def add_to_purchase_history(self, order):
        self.purchase_history.append(order)

class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def compute_total(self):
        return sum(item.price for item in self.items)