# core/greedy/greedy_packer.py
from core.optimizer import Optimizer

class GreedyOptimizer(Optimizer):
    def optimize(self, items, container, config=None):
        sorted_items = sorted(items, key=lambda x: x.value / x.volume, reverse=True)
        packed = []
        used_volume = 0
        for item in sorted_items:
            for _ in range(item.quantity):
                if used_volume + item.volume <= container.volume:
                    packed.append(item)
                    used_volume += item.volume
        return packed
