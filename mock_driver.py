from enum import Enum

from driver import DriverInterface


class MockDriver(DriverInterface):
    def __init__(self):
        pass

    def login(self, username: str, password: str) -> None:
        pass

    def buy(self, code: str, price: int, amount: int) -> None:
        pass

    def sell(self, code: str, price: int, amount: int) -> None:
        pass

    def get_price(self, ticker):
        if ticker == "005930":
            return 50000

        return 1000
