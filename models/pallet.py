class Pallet:
    def __init__(self, length, width, height, max_weight):
        self.length = length
        self.width = width
        self.height = height
        self.max_weight = max_weight
        self.placed_items = []

    def remaining_space(self):
        # Có thể mở rộng thêm nếu bạn muốn tính vùng trống
        return self.length, self.width, self.height

    def current_weight(self):
        return sum(item.item.weight for item in self.placed_items)

    def can_hold(self, item):
        return self.current_weight() + item.weight <= self.max_weight
