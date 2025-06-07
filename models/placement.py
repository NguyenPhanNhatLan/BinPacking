class PackedItemInstance:
    def __init__(self, item, position=(0, 0, 0), rotation=(0, 0, 0)):
        self.item = item
        self.position = position  # (x, y, z) trong container
        self.rotation = rotation  # có thể dùng sau này để xoay item (90/180 độ)

    def __repr__(self):
        return f"PackedItem({self.item.name} at {self.position}, rotated {self.rotation})"