import pytest
from application import AutoTradingSystem
from mock_driver import MockDriver


@pytest.fixture
def system():
    return AutoTradingSystem()


@pytest.fixture
def mock_driver():
    return MockDriver()


def test_select_stock_brocker(system):
    assert system.driver is None

    system.select_stock_brocker("kiwer")
    assert system.driver is not None  # TODO : Device Driver 구현 후 대체, 우선 MockDriver 사용

    system.select_stock_brocker("nemo")
    assert system.driver is not None

    with pytest.raises(ValueError):
        system.select_stock_broker("aa")


def test_login_before_select_stock_brocker(system):
    with pytest.raises(Exception, match="증권사를 먼저 선택해주세요"):
        system.login(id="aa", password="1234")


def test_login_success(system, mock_driver):
    system.driver = mock_driver
    assert system.is_logined is False

    ret = system.login(id="aa", password="1234")

    assert ret is True
    assert system.is_logined is True


def test_buy_without_login_raises_exception(system):
    with pytest.raises(Exception, match="로그인이 필요합니다."):
        system.buy("005930", price=70000, count=10)


def test_successful_buy(system, mock_driver):
    system.driver = mock_driver
    system.is_logined = True

    ret = system.buy("005930", price=70000, count=10)
    assert ret is True


def test_sell_without_login_raises_exception(system):
    with pytest.raises(Exception, match="로그인이 필요합니다."):
        system.sell("005930", price=70000, count=10)


def test_successful_sell(system, mock_driver):
    system.driver = mock_driver
    system.login(id="aa", password=1234)

    ret = system.sell("005930", price=70000, count=10)
    assert ret is True


def test_get_price(system, mock_driver):
    system.driver = mock_driver
    assert system.get_price("005930") == 5000