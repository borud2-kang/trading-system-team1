from mock_driver import MockDriver


class AutoTradingSystem:
    def __init__(self):
        self.driver = None
        self.is_logined = False

    def login(self, id, password) -> bool:
        if self.driver is None :
            raise Exception("증권사를 먼저 선택해주세요")

        print(f"[Auto] login Success")
        self.is_logined = True

        return True

    def buy(self, stock_code, price, count):
        if not self.is_logined:
            raise Exception("로그인이 필요합니다.")
        return self.driver.buy(stock_code, count, price)


    def sell(self, ticker, price, count):
        if not self.is_logined:
            raise Exception("로그인이 필요합니다.")

        return self.driver.sell(ticker, price, count)


    def get_price(self, ticker):
        return self.driver.get_price(ticker)
