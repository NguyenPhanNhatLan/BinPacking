from core.ga.run_ga import GAOptimizer
from core.greedy.greedy_packer import GreedyOptimizer

class OptimizerService:
    def __init__(self, algorithm="ga"):
        if algorithm == "ga":
            self.optimizer = GAOptimizer()
        elif algorithm == "greedy":
            self.optimizer = GreedyOptimizer()
        else:
            raise ValueError("Unsupported algorithm")

    def run(self, items, container, config):
        result = self.optimizer.optimize(items, container, config)
        return result
