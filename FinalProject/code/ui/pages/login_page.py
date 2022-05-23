import allure

from ui.pages.base_page import BasePage

from ui.locators.base_locators import BasePageLocators
from ui.pages.main_page import MainPage
from ui.pages.registration_page import RegistrationPage
from userdata import creds


class LoginPage(BasePage):
    locators = BasePageLocators()
    LOGIN = creds.login
    PASSWORD = creds.password

    @allure.step('Успешная авторизация')
    def auth(self):
        self.send_value(self.locatos.INPUT_USERNAME, creds.login)
        self.send_value(self.locatos.INPUT_PASSWORD, creds.password)
        self.click(self.locatos.BUTTON_LOGIN)
        return MainPage(self.driver)

    @allure.step('Открыть страницу регистрации')
    def go_to_registration_page(self):
        self.click(self.locatos.CREATE_AN_ACCOUNT)
        return RegistrationPage(self.driver)