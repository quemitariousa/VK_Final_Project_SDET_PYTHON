from selenium.webdriver import ActionChains

from ui.locators.base_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_main(self, locator):
        self.click(locator)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def go_home(self):
        self.click(self.locators.BUTTON_HOME)

    def click_logo(self):
        self.click(self.locators.LOGO)

    def logout(self):
        self.click(self.locators.BUTTON_LOGOUT)
        return self.driver

    def go_to_navbar(self, name, link_in):
        name = self.find(name)
        link_in = self.find(link_in)
        ActionChains(self.driver).move_to_element(name).click(
            link_in).perform()
        self.driver.switch_to.window(self.driver.window_handles[-1])