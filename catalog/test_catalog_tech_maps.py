import time
import pytest
from pages.catalog.catalog_tech_maps import TechMaps


"""Справочник/Добавление технологической карты"""
@pytest.mark.skip
def test_catalog_add_tech_maps(test_authorization, driver):
    catalog_tech_maps = TechMaps(driver)
    catalog_tech_maps.open()
    catalog_tech_maps.click_button_add()
    time.sleep(2)
    assert "Добавление технологической карты" == catalog_tech_maps.find_add_text()
    time.sleep(1)
    catalog_tech_maps.find_name().send_keys('Новая технологическая карта')
    catalog_tech_maps.find_sequence_of_work().send_keys('Здесь заполняется последовательность работ')
    catalog_tech_maps.click_button_save_add()
    time.sleep(2)


"""Справочник/Редактировать технологическую карту"""
@pytest.mark.skip
def test_catalog_edit_tech_maps(test_authorization, driver):
    catalog_tech_maps = TechMaps(driver)
    catalog_tech_maps.open()
    catalog_tech_maps.search().send_keys('Новая технологическая карта')
    time.sleep(2)
    catalog_tech_maps.click_button_edit()
    time.sleep(2)
    assert "Изменение данных технологической карты" == catalog_tech_maps.find_edit_text()
    time.sleep(1)
    catalog_tech_maps.find_name().clear()
    catalog_tech_maps.find_sequence_of_work().clear()
    catalog_tech_maps.find_name().send_keys('Редактировал название')
    catalog_tech_maps.find_sequence_of_work().send_keys('Проверка радиального подшипникового узла. Проверка радиально-упорного подшипникового узла. Проверка механизма направляющего аппарата. Проверка уплотнений вентилятора. Запись в Книгу осмотра вентиляторных установок и проверки реверсирования.')
    catalog_tech_maps.click_button_save_edit()
    time.sleep(2)


"""Справочник/Удалить технологическую карту"""
@pytest.mark.skip
def test_catalog_delete_tech_maps(test_authorization, driver):
    catalog_tech_maps = TechMaps(driver)
    catalog_tech_maps.open()
    catalog_tech_maps.search().send_keys('Редактировал название')
    time.sleep(2)
    catalog_tech_maps.click_button_delete()
    time.sleep(2)
    assert "Удаление технологической карты" == catalog_tech_maps.find_delete_text()
    time.sleep(1)
    catalog_tech_maps.click_button_save_delete()
    time.sleep(2)