import logging

import pytest

from tests.scripts.local import start_local_project
from tests.utils.config_reader import Config


@pytest.fixture(scope="session")
def config(request):
    # 從命令行參數中獲取env值
    env = request.config.getoption("--env")
    # 創建config物件
    config = Config(env)
    # 返回config物件
    yield config


@pytest.fixture(scope="session", autouse=True)
def project(request):
    logging.basicConfig(level=logging.INFO, format='- %(levelname)s - %(message)s')

    env = request.config.getoption("--env")
    if env == "local":
        start_local_project()

    yield


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="set environment")
