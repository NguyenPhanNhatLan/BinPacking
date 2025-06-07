class Item:
    def __init__(self, sku, name, category, length, width, height, volume, weight, value,
                 fragile, sensitive, priority, quantity, is_dangerous, max_stack):
        self.sku = sku
        self.name = name
        self.category = category
        self.length = length
        self.width = width
        self.height = height
        self.volume = volume
        self.weight = weight
        self.value = value
        self.fragile = fragile
        self.sensitive = sensitive
        self.priority = priority
        self.quantity = quantity
        self.is_dangerous = is_dangerous
        self.max_stack = max_stack

    def __repr__(self):
        return f"Item({self.name}, {self.value}$, {self.weight}kg)"