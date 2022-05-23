import time

import allure

from ui.locators.base_locators import RegistrationPageLocators
from ui.pages.base_page import BasePage
# from ui.pages.login_page import LoginPage
from utils.builder import Builder


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    @allure.step('Регистрация нового аккаунта')
    def register_new_account(self, name=None, surname=None,
                             middlename=None,
                             username=None, email=None,
                             password=None, accept=True, pw_different=False):
        if name == None: name = Builder.fake_name()
        if surname == None: surname = Builder.fake_name()
        if middlename == None: middlename = Builder.fake_name()
        if username == None: username = Builder.fake_name()
        if email == None: email = Builder.fake_email()
        if password == None: password = Builder.fake_password()

        self.send_value(self.locators.BUTTON_NAME_NEW_ACCOUNT, name)
        self.send_value(self.locators.BUTTON_SURNAME_NEW_ACCOUNT, surname)
        self.send_value(self.locators.BUTTON_MIDDLENAME_NEW_ACCOUNT, middlename)
        self.send_value(self.locators.BUTTON_USERNAME_NEW_ACCOUNT, username)
        self.send_value(self.locators.BUTTON_EMAIL_NEW_ACCOUNT, email)
        self.send_value(self.locators.BUTTON_PASSWORD_NEW_ACCOUNT, password)
        self.send_value(self.locators.BUTTON_REPEAT_PASSWORD_NEW_ACCOUNT,
                        "chtotodrugoe") if pw_different else self.send_value(
            self.locators.BUTTON_REPEAT_PASSWORD_NEW_ACCOUNT, password)
        self.click(self.locators.FLAG_ACCEPT_NEW_ACCOUNT) if accept else self.click(self.locators.BUTTON_REGISTER)
        self.click(self.locators.BUTTON_REGISTER)
        data = {
            "name": name,
            "surname": surname,
            "middle_name": middlename,
            "username": username,
            "password": password,
            "email": email
        }
        return data
