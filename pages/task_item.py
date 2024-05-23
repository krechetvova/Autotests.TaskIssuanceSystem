from pages.base_page import BasePage
from selenium.webdriver.common.by import By


button_add_taskItem_selector = (By.CSS_SELECTOR, '[class="add-item ml-0 ng-star-inserted"]') #Добавить карточку задания
button_add_worker_selector = (By.CSS_SELECTOR, '[title="Добавить сотрудника"]') #Добавить сотрудника в карточку задания
search_worker_selector = (By.CSS_SELECTOR, '[placeholder="Параметры поиска сотрудника"]') #Поиск сотрудника
button_save_worker_selector = (By.CSS_SELECTOR, '[class="btn btn-sm mdl-add-btn"]') #Добавить найденного сотрудника

class TaskItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    """Добавить карточку задания"""
    def button_taskItem(self):
        return self.find(button_add_taskItem_selector)

    def click_button_taskItem(self):
        self.button_taskItem().click()

    """Добавить сотрудника в карточку задания"""
    def button_worker(self):
        return self.find(button_add_worker_selector)

    def click_button_worker(self):
        self.button_worker().click()

    def search_worker(self):
        return self.find(search_worker_selector)

    def send_search_worker(self):
        self.search_worker().send_keys('5')

    def button_save_worker(self):
        return self.find(button_save_worker_selector)

    def click_button_save_worker(self):
        self.button_save_worker().click()

