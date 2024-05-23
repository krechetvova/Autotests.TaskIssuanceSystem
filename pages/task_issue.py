from pages.base_page import BasePage
from selenium.webdriver.common.by import By


button_add_taskIssue_selector = (By.CSS_SELECTOR, '[class="btn btn-sm add-btn ng-star-inserted"]') #добавить наряд
button_delete_taskIssue_selector = (By.CSS_SELECTOR, '[title="Удалить"]') #Удалить наряд
button_delete_yes_taskIssue_selector = (By.CSS_SELECTOR, '[class="btn btn-sm mdl-del-btn"]') #Подтверждение удаления



class Task(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    """Книга нарядов"""
    def open(self):
        self.driver.get('https://demo-tis.abiesys.ru/tasks/task-issues')

    """Создать наряд"""
    def button_add_taskIssue(self):
        return self.find(button_add_taskIssue_selector)

    def click_button_taskIssue(self):
        self.button_add_taskIssue().click()

    """Удалить наряд"""
    def button_delete_taskIssue(self):
        return self.find(button_delete_taskIssue_selector)

    def click_button_delete_taskIssue(self):
        self.button_delete_taskIssue().click()

    def button_delete_yes_taskIssue(self):
        return self.find(button_delete_yes_taskIssue_selector)

    def click_button_delete_yes_taskIssue(self):
        self.button_delete_yes_taskIssue().click()