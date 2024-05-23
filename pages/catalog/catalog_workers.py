from pages.catalog.catalogs import Catalogs
from selenium.webdriver.common.by import By


"""Селекторы полей"""
branch_worker_selector = (By.CSS_SELECTOR, '[name="branchTitle"]')
employeeNumber_worker_selector = (By.CSS_SELECTOR, '[name="employeeNumber"]')
fullName_worker_selector = (By.CSS_SELECTOR, '[name="fullName"]')
workerLamproomId_worker_selector = (By.CSS_SELECTOR,'[name="workerLamproomId"]')
cardCode_worker_selector = (By.CSS_SELECTOR, '[name="cardCode"]')
edsPassword_selector = (By.CSS_SELECTOR,'[name="edsPassword"]')


class CatalogWorkers(Catalogs):

    """Открытие страницы сотрудники"""
    def open(self):
        self.driver.get('https://demo-tis.abiesys.ru/catalogs/workers')

    """Поля"""
    def find_branch(self):
        return self.find(branch_worker_selector)
    def find_employeeNumber(self):
        return self.find(employeeNumber_worker_selector)
    def find_fullName(self):
        return self.find(fullName_worker_selector)
    def find_workerLamproomId(self):
        return self.find(workerLamproomId_worker_selector)
    def find_cardCode(self):
        return self.find(cardCode_worker_selector)
    def find_edsPassword(self):
        return self.find(edsPassword_selector)

