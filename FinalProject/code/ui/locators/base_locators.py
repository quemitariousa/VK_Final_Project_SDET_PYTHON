from selenium.webdriver.common.by import By


class BasePageLocators:
    INPUT_USERNAME = (By.XPATH, '//input[@id = "username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id = "password"]')
    BUTTON_LOGIN = (By.XPATH, '//input[@id = "submit"]')
    CREATE_AN_ACCOUNT = (By.XPATH, '//a[@href= "/reg"]')


class RegistrationPageLocators:
    LINK_TO_REGISTER = (By.XPATH, '//a[text() = "Create an account"]')
    BUTTON_NAME_NEW_ACCOUNT = (By.XPATH, '//input[@id="user_name"]')
    BUTTON_SURNAME_NEW_ACCOUNT = (By.XPATH, '//input[@id="user_surname"]')
    BUTTON_MIDDLENAME_NEW_ACCOUNT = (By.XPATH, '//input[@id="user_middle_name"]')
    BUTTON_USERNAME_NEW_ACCOUNT = (By.XPATH, '//input[@id="username"]')
    MIN_USERNAME = (By.XPATH, '')
    BUTTON_EMAIL_NEW_ACCOUNT = (By.XPATH, '//input[@id="email"]')
    BUTTON_PASSWORD_NEW_ACCOUNT = (By.XPATH, '//input[@id="password"]')
    BUTTON_REPEAT_PASSWORD_NEW_ACCOUNT = (By.XPATH, '//input[@id="confirm"]')
    FLAG_ACCEPT_NEW_ACCOUNT = (By.XPATH, '//input[@id="term"]')
    BUTTON_REGISTER = (By.XPATH, '//input[@id="submit"]')
    LOG_IN_IF_ALREADY = (By.XPATH, '//a[text()="Log in"]')

    NOT_BEAUTIFULL_WARN = (By.XPATH, '//div[@id="flash"]')


class MainPageLocators:
    LOGO = (By.XPATH, '//ul/a[@href= "/"]')

    WHAT_IS_AN_API = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')
    FUTURE_OF_INTERNET = (By.XPATH, '//a[@href="https://www.popularmechanics.com/technology/infrastructure/a29666802'
                                    '/future-of-the-internet/"]')
    LETS_TALK_ABOUT_SMTP = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')

    BUTTON_HOME = (By.XPATH, '//a[text() = "HOME"]')

    BUTTON_PYTHON = (By.XPATH, '//a[@href = "https://www.python.org/"]')
    LINK_PYTHON_HISTORY = (By.XPATH, '//a[@href = "https://en.wikipedia.org/wiki/History_of_Python"]')
    LINK_ABOUT_FLASK = (By.XPATH, '//a[@href = "https://flask.palletsprojects.com/en/1.1.x/#"]')

    BUTTON_LINUX = (By.XPATH, '//a[text() = "Linux"]')
    LINK_DOWNLOAD_CENTOS7 = (By.XPATH, '//a[@href = "https://getfedora.org/ru/workstation/download/"]')

    BUTTON_NETWORK = (By.XPATH, '//a[text() = "Network"]')
    LINK_NEWS = (By.XPATH, '//a[@href = "https://www.wireshark.org/news/"]')
    LINK_DOWNLOAD = (By.XPATH, '//a[@href = "https://www.wireshark.org/#download"]')
    LINK_EXAMPLES = (By.XPATH, '//a[@href = "https://hackertarget.com/tcpdump-examples/"]')

    BUTTON_LOGOUT = (By.XPATH, '//a[@href = "/logout"]')
