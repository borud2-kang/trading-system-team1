class AutoTradingSystem():
    def __init__(self):
        self.driver = None
        self.is_logined = False

    def login(self, id, password) -> bool:
        if self.driver is None :
            raise Exception("증권사를 먼저 선택해주세요")

        print(f"[Auto] login Success")

        self.is_logined = True

        return True

