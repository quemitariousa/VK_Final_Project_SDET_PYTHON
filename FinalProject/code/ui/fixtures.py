import os
import shutil
import sys

import pytest

from ui.pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from ui.pages.login_page import LoginPage


# проблема_параллельности
def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture()
def registration_page(driver, login_page):
    return login_page.go_to_registration_page()


@pytest.fixture()
def main_page(driver, login_page):
    return login_page.auth()


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    return {'url': url, 'browser': browser}

def get_driver(config):
    browser_name = config['browser']

    if browser_name == 'chrome':
        options = ChromeOptions()
        options.set_capability("browserVersion", "100.0")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        caps = {'browserName': browser_name,
                'version': '100.0'
                }

        browser = webdriver.Remote(command_executor=f"http://selenoid:4444/wd/hub",
                                   options=options, desired_capabilities=caps)
    else:
        raise KeyError
    return browser


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = get_driver(config)
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()