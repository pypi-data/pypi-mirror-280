import sys

import mock
import pytest


@pytest.fixture(scope='function', autouse=True)
def cleanup():
    """This fixture removes modules under test from sys.modules.
    This ensures that each module is fully re-imported, along with
    the fixtures for each test function.
    """

    yield None
    try:
        del sys.modules["weatherhat"]
    except KeyError:
        pass


@pytest.fixture(scope='function', autouse=False)
def smbus2():
    """Mock smbus2 module."""

    smbus2 = mock.MagicMock()
    smbus2.i2c_msg.read().__iter__.return_value = [0b00000000]
    sys.modules['smbus2'] = smbus2
    yield smbus2
    del sys.modules['smbus2']


@pytest.fixture(scope="function", autouse=False)
def gpiod():
    """Mock gpiod module."""
    sys.modules["gpiod"] = mock.MagicMock()
    sys.modules["gpiod.line"] = mock.MagicMock()
    yield sys.modules["gpiod"]
    del sys.modules["gpiod"]


@pytest.fixture(scope="function", autouse=False)
def gpiodevice():
    """Mock gpiodevice module."""
    sys.modules["gpiodevice"] = mock.MagicMock()
    sys.modules["gpiodevice"].get_pin.return_value = (mock.Mock(), 0)
    yield sys.modules["gpiodevice"]
    del sys.modules["gpiodevice"]


@pytest.fixture(scope='function', autouse=False)
def bme280():
    sys.modules['bme280'] = mock.MagicMock()
    return sys.modules['bme280']
    del sys.modules["bme280"]


@pytest.fixture(scope='function', autouse=False)
def ltr559():
    sys.modules['ltr559'] = mock.MagicMock()
    return sys.modules['ltr559']
    del sys.modules["ltr559"]


@pytest.fixture(scope='function')
def ioe():
    sys.modules['ioexpander'] = mock.MagicMock()
    return sys.modules['ioexpander']
    del sys.modules["ioexpander"]