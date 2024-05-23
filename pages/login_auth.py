from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from info import *

login_selector = (By.CSS_SELECTOR, '[placeholder="Введите логин"]')
password_selector = (By.CSS_SELECTOR, '[placeholder="Введите пароль"]')
enter_selector = (By.CLASS_NAME, 'btn-block')



class LoginAuth(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    """Открытие браузера"""
    def open(self):
        self.driver.get('https://demo-tis.abiesys.ru/')

    """Поиск поля login"""
    def login(self):
        return self.find(login_selector)

    """Очистка поля login"""

    def clear_login(self):
        return self.login().clear

    """Ввод логина в полен login"""

    def send_login(self):
        self.login().send_keys(cn_login)

    """Поиск поля password"""

    def password(self):
        return self.find(password_selector)

    """Очистка поля login"""

    def clear_password(self):
        return self.password().clear

    """Ввод логина в полен login"""

    def send_password(self):
        self.password().send_keys(cn_password)

    """Поиск кнопки Войти"""

    def button(self):
        return self.find(enter_selector)

    """Нажать кнопку Войти"""

    def click_enter_button(self):
        return self.button().click()
