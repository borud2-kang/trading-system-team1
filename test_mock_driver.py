from mock_driver import MockDriver
from driver import DriverInterface


def test_mock_driver_is_driver_interface():
    driver = MockDriver()

    assert isinstance(driver, DriverInterface)


def test_mock_driver_login_success():
    driver = MockDriver()

    assert driver.login() is True


def test_mock_driver_can_return_price():
    driver = MockDriver()

    price = driver.get_price("005930")

    assert isinstance(price, int)
    assert price > 0


def test_mock_driver_can_buy_stock():
    driver = MockDriver()

    result = driver.buy("005930", count=10, price=70000)

    assert result is True


def test_mock_driver_can_sell_stock():
    driver = MockDriver()

    result = driver.sell("005930", count=5, price=71000)

    assert result is True