from pages.base_page import BasePage
from selenium.webdriver.common.by import By

"""Селекторы кнопок"""
button_add_selector = (By.CSS_SELECTOR, '[class="btn btn-sm add-btn ng-star-inserted"]')
button_edit_selector = (By.CSS_SELECTOR, '[title= "Изменить"]')
button_delete_selector = (By.CSS_SELECTOR, '[title= "Удалить"]')

"""Селекторы кнопок в окне"""
button_save_add_selector = (By.CSS_SELECTOR, '[class = "btn btn-sm mdl-add-btn ng-star-inserted"]')
button_save_edit_selector = (By.CSS_SELECTOR, '[class = "btn btn-sm mdl-edit-btn ng-star-inserted"]')
button_save_delete_selector = (By.CSS_SELECTOR, '[class = "btn btn-sm mdl-del-btn ng-star-inserted"]')

"""Селектор. Заголовки."""
add_text_selector = (By.TAG_NAME, 'h3')
edit_text_selector = (By.TAG_NAME, 'h3')
delete_text_selector = (By.TAG_NAME, 'h3')


search_selector = (By.CSS_SELECTOR,'[placeholder= "Поиск"]')


class Catalogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    """Добавить"""
    def button_add(self):
        return self.find(button_add_selector)
    def click_button_add(self):
        self.button_add().click()

    """Изменить"""
    def button_edit(self):
        return self.find(button_edit_selector)
    def click_button_edit(self):
        self.button_edit().click()

    """Удалить"""
    def button_delete(self):
        return self.find(button_delete_selector)
    def click_button_delete(self):
        self.button_delete().click()


    """Подтверждение добавления/редактирования/удаления"""
    def button_save_add(self):
        return self.find(button_save_add_selector)
    def click_button_save_add(self):
        self.button_save_add().click()

    def button_save_edit(self):
        return self.find(button_save_edit_selector)
    def click_button_save_edit(self):
        self.button_save_edit().click()

    def button_save_delete(self):
        return self.find(button_save_delete_selector)
    def click_button_save_delete(self):
        self.button_save_delete().click()

    """Заголовки. Текст."""
    def find_add_text(self):
        return self.find(add_text_selector).text
    def find_edit_text(self):
        return self.find(edit_text_selector).text
    def find_delete_text(self):
        return self.find(delete_text_selector).text

    """Поиск"""
    def search(self):
        return self.find(search_selector)