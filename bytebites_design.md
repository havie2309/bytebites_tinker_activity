┌─────────────────────────────────┐
│          Customer               │
├─────────────────────────────────┤
│ Attributes:                     │
│ - name: String                  │
│ - purchaseHistory: List<Order>  │
├─────────────────────────────────┤
│ Methods:                        │
│ + addToPurchaseHistory(o: Order)│
└─────────────────────────────────┘
           │
           │ references
           │ (purchases)
           ▼
┌─────────────────────────────────┐
│          Order                  │
├─────────────────────────────────┤
│ Attributes:                     │
│ - items: List<MenuItem>         │
├─────────────────────────────────┤
│ Methods:                        │
│ + add_item(item: MenuItem)      │
│ + compute_total(): Decimal      │
└─────────────────────────────────┘
           │
           │ contains
           │ (multiple items)
           ▼
┌─────────────────────────────────┐
│         MenuItem                │
├─────────────────────────────────┤
│ Attributes:                     │
│ - name: String                  │
│ - price: Decimal                │
│ - category: String              │
│ - popularity_rating: Double     │
└─────────────────────────────────┘
           ▲
           │
           │ contains
           │ (collection of items)
           │
┌─────────────────────────────────┐
│          Menu                   │
├─────────────────────────────────┤
│ Attributes:                     │
│ - items: List<MenuItem>         │
├─────────────────────────────────┤
│ Methods:                        │
│ + add_item(item: MenuItem)      │
│ + filter_by_category(cat: String)
│   → List<MenuItem>              │
└─────────────────────────────────┘