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


def test_login(system, mock_driver):
    system.driver = mock_driver
    assert system.is_logined is False

    ret = system.login(id="aa", password=1234)

    mock_driver.login.assert_called_once_with(id="aa", password=1234)
    assert ret is True
    assert system.is_logined is True