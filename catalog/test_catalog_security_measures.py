import time
import pytest
from pages.catalog.catalog_security_measures import SecurityMeasures


"""Справочник/Добавление меры безопасности"""
@pytest.mark.skip
def test_catalog_add_security_measures(test_authorization, driver):
    catalog_security_measures = SecurityMeasures(driver)
    catalog_security_measures.open()
    catalog_security_measures.click_button_add()
    time.sleep(2)
    assert "Добавление меры безопасности" == catalog_security_measures.find_add_text()
    time.sleep(1)
    catalog_security_measures.find_description().send_keys('Выход на рабочее место только в одежде')
    catalog_security_measures.click_button_save_add()
    time.sleep(2)


"""Справочник/Редактировать меры безопасности"""
@pytest.mark.skip
def test_catalog_edit_security_measures(test_authorization, driver):
    catalog_security_measures = SecurityMeasures(driver)
    catalog_security_measures.open()
    catalog_security_measures.search().send_keys('Выход на рабочее место только в одежде')
    time.sleep(2)
    catalog_security_measures.click_button_edit()
    time.sleep(2)
    assert "Изменение данных меры безопасности" == catalog_security_measures.find_edit_text()
    time.sleep(1)
    catalog_security_measures.find_description().clear()
    catalog_security_measures.find_description().send_keys('Данные указал верно. Всё безопасно.')
    catalog_security_measures.click_button_save_edit()
    time.sleep(2)


"""Справочник/Удалить меры безопасности"""
@pytest.mark.skip
def test_catalog_delete_security_measures(test_authorization, driver):
    catalog_security_measures = SecurityMeasures(driver)
    catalog_security_measures.open()
    catalog_security_measures.search().send_keys('Данные указал верно. Всё безопасно.')
    time.sleep(2)
    catalog_security_measures.click_button_delete()
    time.sleep(2)
    assert "Удаление меры безопасности" == catalog_security_measures.find_delete_text()
    time.sleep(1)
    catalog_security_measures.click_button_save_delete()
    time.sleep(2)


