from driver import DriverInterface


class MockDriver():

    def login(self, id: str, password: str) -> bool:
        print(id + ' login success')
        return True

    def buy(self, stock_code:str, count:int, price:float ) -> bool :
        print(stock_code + ' : Buy stock ( ' + str(price) + ' * ' + str(count))
        return True
