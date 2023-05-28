from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def observe(self, result):
        pass

class MyObserver(Observer):
    def observe(self, result):
        print(result)





