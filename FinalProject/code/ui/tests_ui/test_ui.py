# import pdb
# import time
#
# import allure
# import pytest
#
# from ui.tests_ui.base import BaseCase
# from ui.locators.base_locators import MainPageLocators
#
#
# class TestsRegisterUser(BaseCase):
#
#      #баг, миднейм энивей NULL
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации корректного юзера c middlename')
#     @pytest.mark.xfail
#     def test_correct_user_with_mn(self, registration_page):
#         new_user = registration_page.register_new_account()
#         assert f"Logged as {new_user['username']}" in self.driver.page_source
#         assert new_user['middle_name'] == self.mysql_client.get_users_by_username(new_user['username'])[0].middle_name
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации корректного юзера без middlename')
#     def test_correct_user_without_mn(self, registration_page):
#         new_user = registration_page.register_new_account(middlename="")
#         assert f"Logged as {new_user['username']}" in self.driver.page_source
#         assert None == self.mysql_client.get_users_by_username(new_user['username'])[0].middle_name
#         assert "Internal Server Error" not in self.driver.page_source
#
#      # баг, обрезается юзернейм(
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c большим username')
#     @pytest.mark.xfail
#     def test_incorrect_long_username(self, registration_page):
#         registration_page.register_new_account(username="privetktosmotrit" * 100)
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c username из одного символа')
#     def test_incorrect_short_1_username(self, registration_page):
#         registration_page.register_new_account(username="R")
#         assert registration_page.find(registration_page.locators.BUTTON_USERNAME_NEW_ACCOUNT).get_attribute(
#             'validationMessage') == f"Текст должен быть не короче 6\xa0симв. Длина текста сейчас: 1\xa0символ."
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c username из двух символов')
#     def test_incorrect_short_2_username(self, registration_page):
#         user = registration_page.register_new_account(username="RR")
#         username = user['username']
#         assert registration_page.find(registration_page.locators.BUTTON_USERNAME_NEW_ACCOUNT).get_attribute(
#             'validationMessage') == f"Минимально допустимое количество символов: 6. Длина текста сейчас: {len(username)}."
#         assert "Internal Server Error" not in self.driver.page_source
#
#      # cоздается пользователь при лимите name
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c некорректным name - БАГ')
#     @pytest.mark.xfail
#     @pytest.mark.parametrize("name", [" ", (
#             "NADO256SIMVOLOVSORRY" * 100)],
#                              ids=["empty_name", "long_name"])
#     def test_incorrect_name(self, registration_page, name):
#         user = registration_page.register_new_account(name=name)
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert len(self.mysql_client.get_users_by_username(user['username'])) == 0
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c пустым name - БАГ warning с фамилией')
#     @pytest.mark.xfail
#     def test_empty_name_beautifull_warn(self, registration_page):
#         user = registration_page.register_new_account(name=" ")
#         # тут появляется хуйня с фамилией нормальная
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert "Некорректная фамилия" not in self.driver.page_source
#         assert len(self.mysql_client.get_users_by_username(user['username'])) == 0
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c пустым name - БАГ warning с фамилией некрасивый')
#     @pytest.mark.xfail
#     def test_empty_name_not_beautifull_warn(self, registration_page):
#         user = registration_page.register_new_account(name=" ", email="hahahehe")
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert len(self.mysql_client.get_users_by_username(user['username'])) == 0
#         # assert "{'name': ['Некорректная фамилия'], 'email': ['Invalid email address']}" not in self.driver.page_source
#         assert not registration_page.find(registration_page.locators.NOT_BEAUTIFULL_WARN, 10)
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c некорректным surname - БАГ')
#     @pytest.mark.xfail
#     @pytest.mark.parametrize("surname", [" ", "1", (
#             "NADO256SIMVOLOVSORRY" * 100)],
#                              ids=["empty_surname", "short_surname", "long_surname"])
#     def test_incorrect_surname(self, registration_page, surname):
#         user = registration_page.register_new_account(surname=surname)
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert 0 == len(self.mysql_client.get_users_by_username(user['username']))
#         assert "Internal Server Error" not in self.driver.page_source
#
#      # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c некорректным email - БАГ')
#     @pytest.mark.xfail
#     @pytest.mark.parametrize("email", [" ", "1", (
#             "NADO256SIMVOLOVSORRY" * 100), "privetgavyandex.ru"],
#                              ids=["empty_email", "short_email", "long_email", "email_wothout_doge"])
#     def test_incorrect_email(self, registration_page, email):
#         user = registration_page.register_new_account(email=email)
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert 0 == len(self.mysql_client.get_users_by_username(user['username']))
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера c некорректным password - БАГ')
#     @pytest.mark.xfail
#     @pytest.mark.parametrize("pw", [" ", "1", (
#             "NADO256SIMVOLOVSORRY" * 100)],
#                              ids=["empty_pw", "short_pw", "long_pw"])
#     def test_incorrect_pw(self, registration_page, pw):
#         user = registration_page.register_new_account(password=pw)
#         time.sleep(2)
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert 0 == len(self.mysql_client.get_users_by_username(user['username']))
#         assert "Internal Server Error" not in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера без обязательного флага подтверждения')
#     def test_without_accept(self, registration_page):
#         registration_page.register_new_account(accept=False)
#         assert registration_page.find(registration_page.locators.FLAG_ACCEPT_NEW_ACCOUNT).get_attribute(
#             'validationMessage') == f"Чтобы продолжить, установите этот флажок."
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера с разными паролями')
#     def test_dif_pw(self, registration_page):
#         registration_page.register_new_account(pw_different=True)
#         assert "Passwords must match" in self.driver.page_source
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#
#     @allure.epic('UI tests')
#     @allure.feature('Register user')
#     @allure.description('Проверка регистрации юзера пропущенными обязательными полями')
#     def test_empty_required_fields(self, registration_page):
#         registration_page.register_new_account(username="", password="", email="", surname="", name="")
#         assert self.driver.current_url != "http://test_app:8086/welcome/"
#         assert registration_page.find(registration_page.locators.BUTTON_NAME_NEW_ACCOUNT).get_attribute(
#             'validationMessage') == f"Заполните это поле."
#         registration_page.register_new_account(username="", password="", email="", surname="")
#         assert registration_page.find(registration_page.locators.BUTTON_SURNAME_NEW_ACCOUNT).get_attribute(
#             'validationMessage') == f"Заполните это поле."
#         registration_page.register_new_account(username="", password="", email="")
#         assert registration_page.find(registration_page.locators.BUTTON_USERNAME_NEW_ACCOUNT).get_attribute(
#             'validationMessage') == f"Заполните это поле."
#         registration_page.register_new_account(password="", email="")
#         assert registration_page.find(registration_page.locators.BUTTON_PASSWORD_NEW_ACCOUNT).get_attribute(
#             'validationMessage') == f"Заполните это поле."
#         registration_page.register_new_account(email="")
#         assert "Incorrect email length" in self.driver.page_source
#
# class TestsAuth(BaseCase):
#
#     @allure.epic('UI tests')
#     @allure.feature('Authorization')
#     @allure.description('Проверка корректного логина')
#     def test_login(self, username="quemitariousa6", password="ilovebordercollie"):
#         self.base_page.auth(username, password)
#         assert f"Logged as {username}" in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Authorization')
#     @allure.description('Проверка логина с неправильными данными')
#     def test_incorrect_login(self, username="hahahehe", password="hahahehe"):
#         self.base_page.auth(username, password)
#         time.sleep(2)
#         assert "Invalid username or password" in self.driver.page_source
#
#
# class TestsMainPage(BaseCase):
#     @allure.epic('UI tests')
#     @allure.feature('Main page')
#     @allure.description('Проверка навбара')
#     @pytest.mark.parametrize("link, name_in_link, url_to_be", [(MainPageLocators.BUTTON_PYTHON,
#                                                                 MainPageLocators.LINK_PYTHON_HISTORY,
#                                                                 "https://en.wikipedia.org/wiki/History_of_Python"),
#                                                                (MainPageLocators.BUTTON_PYTHON,
#                                                                 MainPageLocators.LINK_ABOUT_FLASK,
#                                                                 "https://flask.palletsprojects.com/en/1.1.x/#"),
#                                                                (MainPageLocators.BUTTON_LINUX,
#                                                                 MainPageLocators.LINK_DOWNLOAD_CENTOS7,
#                                                                 "https://www.centos.org/download/"),
#                                                                (MainPageLocators.BUTTON_NETWORK,
#                                                                 MainPageLocators.LINK_NEWS,
#                                                                 "https://www.wireshark.org/news/"),
#                                                                (MainPageLocators.BUTTON_NETWORK,
#                                                                 MainPageLocators.LINK_DOWNLOAD,
#                                                                 "https://www.wireshark.org/#download"),
#                                                                (MainPageLocators.BUTTON_NETWORK,
#                                                                 MainPageLocators.LINK_EXAMPLES,
#                                                                 "https://hackertarget.com/tcpdump-examples/")
#                                                                ],
#                              ids=['wiki', 'flask', 'centos7', 'wireshark_news', 'wireshark_download', 'hackertarget'])
#     def test_navbar(self, main_page, link, name_in_link, url_to_be):
#         main_page.go_to_navbar(link, name_in_link)
#         new_link = self.driver.current_url
#         assert new_link == url_to_be
#
#     @allure.epic('UI tests')
#     @allure.feature('Main page')
#     @allure.description('Проверка основных кнопок')
#     @pytest.mark.parametrize("picture, url_to_be",
#                              [(MainPageLocators.WHAT_IS_AN_API, "https://en.wikipedia.org/wiki/API"),
#                               (MainPageLocators.FUTURE_OF_INTERNET,
#                                "https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the"
#                                "-internet/"),
#                               (MainPageLocators.LETS_TALK_ABOUT_SMTP, "https://ru.wikipedia.org/wiki/SMTP")],
#                              ids=['wiki', 'future', 'smtp'])
#     def test_main(self, main_page, picture, url_to_be):
#         main_page.go_to_main(picture)
#         new_link = self.driver.current_url
#         assert new_link == url_to_be
#
#     @allure.epic('UI tests')
#     @allure.feature('Main page')
#     @allure.description('Проверка логаута')
#     def test_logout(self, main_page):
#         main_page.logout()
#         assert self.driver.current_url == 'http://test_app:8086/login'
#         assert "Welcome to the TEST SERVER" in self.driver.page_source
#
#     @allure.epic('UI tests')
#     @allure.feature('Main page')
#     @allure.description('Проверка кнопки home')
#     def test_home(self, main_page):
#         main_page.go_home()
#         assert self.driver.current_url == 'http://test_app:8086/welcome/'
#
#     @allure.epic('UI tests')
#     @allure.feature('Main page')
#     @allure.description('Проверка кнопки Python - БАГ')
#
#     def test_python_button(self, main_page):
#         main_page.click(main_page.locators.BUTTON_PYTHON)
#         assert self.driver.current_url == 'http://test_app:8086/welcome/'
