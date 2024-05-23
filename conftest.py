import time
import pytest
from selenium import webdriver
from pages.login_auth import LoginAuth

"""Подключение Selenium"""
@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser

"""Авторизация"""
@pytest.fixture()
def test_authorization(driver):
    login_auth = LoginAuth(driver)
    login_auth.open()
    login_auth.clear_login()
    login_auth.send_login()
    login_auth.clear_password()
    login_auth.send_password()
    login_auth.click_enter_button()
    time.sleep(2)

