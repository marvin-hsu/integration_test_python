import subprocess

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


@pytest.fixture(scope="session", autouse=True)
def project(request):
    env = request.config.getoption("--env")
    if env == "local":

        # 在測試開始前啟動src中專案
        cmd = ["python", "-u", "-m", "src.demo"]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)

        # 等待 process 打印 "Hello World!
        while True:
            line = process.stdout.readline()
            if line.strip() == "Hello World!":
                break

    yield


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="set environment")
