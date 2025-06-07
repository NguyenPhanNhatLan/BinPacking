from models.placement import PackedItemInstance
from models.pallet import Pallet

class PalletPackingEngine:
    def __init__(self, pallet):
        self.pallet = pallet
        self.placed_items = []

    def can_place(self, item, position):
        x, y, z = position

        if (x + item.length > self.pallet.length or
            y + item.width > self.pallet.width or
            z + item.height > self.pallet.height):
            return False

        for placed in self.placed_items:
            px, py, pz = placed.position
            if (x < px + placed.item.length and x + item.length > px and
                y < py + placed.item.width and y + item.width > py and
                z < pz + placed.item.height and z + item.height > pz):
                return False

        return True

    def place_item(self, item):
        for z in range(0, self.pallet.height - item.height + 1):
            for y in range(0, self.pallet.width - item.width + 1):
                for x in range(0, self.pallet.length - item.length + 1):
                    if self.can_place(item, (x, y, z)) and self.pallet.can_hold(item):
                        packed = PackedItemInstance(item, (x, y, z))
                        self.placed_items.append(packed)
                        self.pallet.placed_items.append(packed)
                        return packed
        return None

    def pack_items(self, items, ins = 0.04):
        packed = []
        for item in items:
            result = self.place_item(item)
            if result:
                packed.append(result)
        return packed

class PackingEngine:
    def __init__(self, container):
        self.container = container

    def pack_items(self, items):
        packed = []
        for pallet in self.container.pallets:
            engine = PalletPackingEngine(pallet)
            packed_items = engine.pack_items(items)
            packed.extend(packed_items)
        return packed