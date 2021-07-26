import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=['chrome', 'firefox', 'opera'])
    parser.addoption("--url", action="store", default="https://www.cp.pt/passageiros/en")
    parser.addoption("--executor", action="store", default="127.0.0.1", help="Insert IP address of machine")
    parser.addoption("--bversion", action="store", default="91.0")
    parser.addoption("--vnc", action="store_true", default=False)


@pytest.fixture()
def browser(request):
    # Taking parameters from console which helps to set browser,url and executor
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    browser_version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")

    executor_url = f"http://{executor}:4444/wd/hub"

    capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": vnc
        }
    }

    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
    driver.url = url

    def end():
        driver.quit()

    request.addfinalizer(end)

    return driver
