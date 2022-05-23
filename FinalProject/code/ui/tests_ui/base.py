import pytest
from mysql.sql.builder import MysqlBuilder
from ui.fixtures import *
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage

CLICK_RETRY = 3


class BaseCase:
    driver = None
    config = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, mysql_client, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.mysql_client = mysql_client
        self.builder = MysqlBuilder(self.mysql_client)

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        # self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        # self.main_page: MainPage = (request.getfixturevalue('main_page'))
        # self.registration_page: RegistrationPage = (request.getfixturevalue('registration_page'))
