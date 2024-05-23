from pages.catalog.catalogs import Catalogs
from selenium.webdriver.common.by import By

name_selector = (By.CSS_SELECTOR, '[placeholder="Введите наименование"]')
sequence_of_work_selector = (By.CSS_SELECTOR, '[placeholder="Введите последовательность работ"]')

class TechMaps(Catalogs):

    def open(self):
        self.driver.get("https://demo-tis.abiesys.ru/catalogs/tech-maps")


    def find_name(self):
        return self.find(name_selector)

    def find_sequence_of_work(self):
        return self.find(sequence_of_work_selector)

