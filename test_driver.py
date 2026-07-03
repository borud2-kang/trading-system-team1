import pytest
from driver import DriverInterface


def test_driver_interface_cannot_be_instantiated():
    with pytest.raises(TypeError):
        DriverInterface()


def test_driver_interface_requires_methods():
    required = ["login", "buy", "sell", "get_price"]

    for method in required:
        assert hasattr(DriverInterface, method)

