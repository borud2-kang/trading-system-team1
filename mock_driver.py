from driver import DriverInterface


class MockDriver(DriverInterface):
    def login(self, id, password):
        pass

    def buy(self, stock_code, count, price):
        pass

    def sell(self, stock_code, count, price):
        print('[MOCK]' + stock_code + ' sell stock ( price : ' + str(price) + ' ) * ( count : ' + str(count) + ')')
        return True

    def get_price(self, stock_code):
        pass
