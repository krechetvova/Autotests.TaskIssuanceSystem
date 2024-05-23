import time
import pytest
from pages.catalog.catalog_workers import *
from pages.catalog.catalogs import *
from selenium.webdriver.support.wait import WebDriverWait  #явное ожидание
from selenium.webdriver.support import expected_conditions as EC #условия, по которым происходит ожидание


"""Справочник/Создание нового сотрудника"""
@pytest.mark.skip
def test_catalog_add_workers(test_authorization, driver):
    catalog_workers = CatalogWorkers(driver)
    catalog_workers.open()
    catalog_workers.click_button_add()
    WebDriverWait(driver, 10).until((EC.text_to_be_present_in_element(add_text_selector, 'Добавление сотрудника')))
    assert catalog_workers.find_add_text() == 'Добавление сотрудника'
    catalog_workers.find_branch().send_keys('ПОЕЗДА')
    catalog_workers.find_employeeNumber().send_keys('8080')
    catalog_workers.find_fullName().send_keys('Рехтин Геннадий Васильевич')
    catalog_workers.click_button_save_add()
    assert driver.find_element(By.CSS_SELECTOR, '[role="dialog"]').size == 0
    time.sleep(2)

"""Справочник/Редактировать сотрудника"""

def test_catalog_edit_workers(test_authorization, driver):
    catalog_worker = CatalogWorkers(driver)
    catalog_worker.open()
    catalog_worker.search().send_keys('РЕХТИН ГЕННАДИЙ ВАСИЛЬЕВИЧ')
    time.sleep(2)
    catalog_worker.click_button_edit()
    WebDriverWait(driver, 10).until((EC.text_to_be_present_in_element(add_text_selector, 'Изменение данных сотрудника')))
    assert catalog_worker.find_edit_text() == 'Изменение данных сотрудника'
    time.sleep(1)
    catalog_worker.find_workerLamproomId().send_keys('9982')
    catalog_worker.find_cardCode().send_keys('2183971293812938')
    catalog_worker.find_edsPassword().send_keys('123')
    catalog_worker.click_button_save_edit()
    time.sleep(2)



