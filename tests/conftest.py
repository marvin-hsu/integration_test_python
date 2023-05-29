import pytest

from tests.utils.config_reader import Config


@pytest.fixture(scope="session")
def config(request):
    # 從命令行參數中獲取env值
    env = request.config.getoption("--env")
    # 創建config物件
    config = Config(env)
    # 返回config物件
    yield config


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="set environment")
