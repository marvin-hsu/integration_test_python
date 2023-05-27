@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    config = Config(env)
    yield config

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="set environment")