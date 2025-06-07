from abc import ABC, abstractmethod

class Optimizer(ABC):
    @abstractmethod
    def optimize(self, items, container, config):
        """Tối ưu danh sách items cho container, trả về danh sách sắp xếp"""
        pass