from stock_broker_driver import StockBrokerDriver

class MockStockBrokerDriver(StockBrokerDriver):
    def __init__(self):
        print("Mock Stock Broker Driver가 생성되었습니다.")

    def login(self, username, password):
        print(f"username: {username}, password: {password}")

    def buy(self, code, amount, price):
        print(f"buy {code} with {amount} at {price}")

    def sell(self, code, amount, price):
        print(f"sell {code} with {amount} at {price}")

    def get_price(self, code):
        print(f"get price for {code}")