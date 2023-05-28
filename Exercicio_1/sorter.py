# Interface
from abc import ABC, abstractmethod

class Sorter(ABC):
    @abstractmethod
    def sort(self, arr):
        pass
