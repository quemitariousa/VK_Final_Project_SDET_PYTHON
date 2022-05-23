import string
import time
import random

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.base_locators import BasePageLocators
from utils.builder import Builder


class PageNotOpenedException(Exception):
    pass


CLICK_RETRY = 5
PORT = 8086


class BasePage():
    locatos = BasePageLocators
    url = f'http://app:{PORT}/'

    def __init__(self, driver):
        self.driver = driver

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=5) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def send_value(self, locator, value):
        input_element = self.wait_find(locator)
        input_element.clear()
        input_element.send_keys(value)

    def wait_find(self, locator):
        WebDriverWait(self.driver, timeout=5).until(
            lambda d: self.find(locator))
        return self.find(locator)

    def randStr(self, chars=string.ascii_uppercase + string.digits, N=10):
        return ''.join(random.choice(chars) for _ in range(N))

    def send_file(self, locator, file):
        input_element = self.wait_find(locator)
        for i in range(CLICK_RETRY):
            try:
                input_element.send_keys(file)
            except ElementNotInteractableException:
                pass

    def auth(self, username, password):
        self.send_value(self.locatos.INPUT_USERNAME, username)
        self.send_value(self.locatos.INPUT_PASSWORD, password)
        self.click(self.locatos.BUTTON_LOGIN)
        return self.driver


