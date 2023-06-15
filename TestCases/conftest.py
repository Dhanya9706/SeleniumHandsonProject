import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def setup(browser):
    if browser == 'chrome':
        serv_ob=Service("D:\\Project\\LatestChrome\\chromedriver.exe")
        ops = webdriver.ChromeOptions()
        ops.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=serv_ob,options=ops)
        return driver
    elif browser == 'chromeheadless':
        serv_ob = Service("D:\\Project\\LatestChrome\\chromedriver.exe")
        ops = webdriver.ChromeOptions()
        ops.add_argument("--disable-notifications")
        ops.add_argument('--headless')
        driver = webdriver.Chrome(service=serv_ob, options=ops)
        return driver
    elif browser == 'edge':
        serv_obj = Service("D:\\Project\\edge\\msedgedriver.exe")
        ops = webdriver.EdgeOptions()
        ops.add_argument('--disable-notifications')
        driver = webdriver.Edge(service=serv_obj,options=ops)
        return driver
    else:
        serv_obj = Service("D:\\Project\\edge\\msedgedriver.exe")
        ops = webdriver.EdgeOptions()
        ops.add_argument('--disable-notifications')
        ops.add_argument('--headless')
        driver = webdriver.Edge(service=serv_obj, options=ops)
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--browser")

def  pytest_configure(config):
    config._metadata = {"Project Name" : 'Selenium Handson Project',
                        "Module Name" : 'Login:Items',
                        "Tester" :'Yashu'}

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
