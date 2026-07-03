import pytest

from mock_driver import MockStockBrokerDriver

DRIVER_TYPE="mock"
USERNAME="username"
PASSWORD="password"

@pytest.fixture
def setup_driver():
    if DRIVER_TYPE=="kiwer": pass
    elif DRIVER_TYPE=="nemo": pass
    return MockStockBrokerDriver()

def test_login(setup_driver, capsys):
    # arrange
    driver = setup_driver

    # act
    driver.login(USERNAME, PASSWORD)

    # assert
    assert capsys.readouterr().out == f"username: {USERNAME}, password: {PASSWORD}\n"