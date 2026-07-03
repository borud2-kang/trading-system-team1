from mock_driver import MockDriver


class AutoTradingSystem:
    def __init__(self):
        self.driver = MockDriver()
        self.is_logined = False

    def login(self, id, password):
        pass

    def buy(self, stock_code, price, count):
        if not self.is_logined:
            raise Exception("로그인이 필요합니다.")
        return self.driver.buy(stock_code, count, price)

    def sell(self, stock_code, price, count):
        pass
