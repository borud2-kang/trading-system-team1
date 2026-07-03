from abc import ABC, abstractmethod

class DriverInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def login(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def buy(self, code: str, price: int, amount: int) -> None:
        pass

    @abstractmethod
    def sell(self, code: str, price: int, amount: int) -> None:
        pass

    @abstractmethod
    def get_price(self, code: str) -> int:
        pass