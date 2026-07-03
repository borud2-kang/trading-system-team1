from enum import Enum

from driver import DriverInterface


class MockDriver(DriverInterface):
    def __init__(self):
        pass

    def login(self, id: str, password: str) -> bool:
        print(id + ' login success')
        return True

    def buy(self, stock_code:str, count:int, price:float ) -> bool :
        print(stock_code + ' : Buy stock ( ' + str(price) + ' * ' + str(count))
        return True

    def sell(self, code: str, price: int, amount: int) -> None:
        pass

    def get_price(self, ticker):
        if ticker == "005930":
            return 50000

        return 1000
