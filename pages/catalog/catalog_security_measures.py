from pages.catalog.catalogs import Catalogs
from selenium.webdriver.common.by import By



description_selector = (By.CSS_SELECTOR, '[placeholder="Введите описание"]')


class SecurityMeasures(Catalogs):

    """Открытие страницы меры безопасности"""
    def open(self):
        self.driver.get('https://demo-tis.abiesys.ru/catalogs/security-measures')


    """Описание"""
    def find_description(self):
        return self.find(description_selector)



