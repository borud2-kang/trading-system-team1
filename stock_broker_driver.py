from abc import ABC, abstractmethod

class StockBrokerDriver(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def login(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def buy(self, code: str, amount: int, price: int) -> None:
        pass

    @abstractmethod
    def sell(self, code: str, amount: int, price: int) -> None:
        pass

    @abstractmethod
    def get_price(self, code: str) -> int:
        pass
