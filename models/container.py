class Container:
    def __init__(self, length, width, height, max_weight, pallets=None):
        self.length = length
        self.width = width
        self.height = height
        self.max_weight = max_weight
        self.pallets = pallets if pallets else []  # List[Pallet]

    def __repr__(self):
        return f"Container({self.length}x{self.width}x{self.height}, max {self.max_weight}kg)"