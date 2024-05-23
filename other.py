import time

from selenium.webdriver.common.by import By

# from time import sleep





"""Авторизация"""


"""Переход в книгу нарядов. Добавление наряда."""
def test_add_taskIssue(test_login):
    driver.find_element(By.XPATH, '//a[@routerlink="tasks/task-issues"]').click()
    driver.find_element(By.CSS_SELECTOR, '[title="Удалить"]').click()
    driver.find_element(By.CSS_SELECTOR, '[class = "btn btn-sm mdl-del-btn"]').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-sm add-btn ng-star-inserted"]').click()
    time.sleep(4)

#
#
#
# """Добавить ответственного сотрудника. Наряд выдал."""
# add_issuedAnOutfit = driver.find_element(By.XPATH, '//label[text()="Наряд выдал"]/following-sibling::a[@class="btn-resp btn-resp-add ng-star-inserted"]').click()
# time.sleep(2)
#
# """Поиск сотрудника"""
# search_worker = driver.find_element(By.NAME, 'workerSearch')
# search_worker.send_keys('90052')
# time.sleep(2)
#
# """Добавить найденного сотрудника в карточку задания"""
# add_search_worker = driver.find_element(By.XPATH, '//button[@class="btn btn-sm mdl-add-btn"]').click()
# time.sleep(4)
#
# """Добавить ответственного сотрудника. Наряд принял."""
# add_acceptedTheOutfit = driver.find_element(By.XPATH, '//label[text()="Наряд принял"]/following-sibling::a[@class="btn-resp btn-resp-add ng-star-inserted"]').click()
# time.sleep(2)
# """Поиск сотрудника"""
# search_worker = driver.find_element(By.NAME, 'workerSearch')
# search_worker.send_keys('4070')
# time.sleep(2)
# """Добавить найденного сотрудника в карточку задания"""
# add_search_worker = driver.find_element(By.XPATH, '//button[@class="btn btn-sm mdl-add-btn"]').click()
# time.sleep(4)
#
#
#
# """Добавить карточку задания"""
# add_task_item = driver.find_element(By.XPATH, '//a[@class="add-item ml-0 ng-star-inserted"]').click()
# time.sleep(1)
#
#
# """Добавление сотрудника в карточку задания"""
# add_worker = driver.find_element(By.XPATH, '//a[@type="button"][@title="Добавить сотрудника"]').click()
# time.sleep(2)
#
# """Поиск сотрудника"""
# search_worker = driver.find_element(By.NAME, 'workerSearch')
# search_worker.send_keys('5504')
# time.sleep(2)
#
# """Добавить найденного сотрудника в карточку задания"""
# add_search_worker = driver.find_element(By.XPATH, '//button[@class="btn btn-sm mdl-add-btn"]').click()
# time.sleep(2)
#
# """Добавление задания в карточку задания"""
# add_task = driver.find_element(By.XPATH, '//a[@type="button"][@title="Добавить задание"]').click()
# time.sleep(2)
#
#
#
# """Рабочее место"""
# #Поиск рабочего места из списка
# work_place = driver.find_element(By.XPATH, '//*[@bindvalue="id"]/descendant::input[@type="text"]')
# work_place.send_keys('Конвейерный штрек 5а-7-36')
# time.sleep(2)
# work_place.send_keys(Keys.ENTER)
# time.sleep(2)
#
# """Вид выполняемых работ"""
# #Поиск рабочего места из списка
# work_type = driver.find_element(By.XPATH, '//*[@bindvalue="workTypeId"]/descendant::input[@type="text"]')
# work_type.send_keys('Монтаж балки ПМП')
# time.sleep(1)
# work_type.send_keys(Keys.ENTER)
# time.sleep(1)
#
# """Единица измерения"""
# #Поиск рабочего места из списка
# unit = driver.find_element(By.XPATH, '//label[text()="Ед. изм."]/following::input[@aria-autocomplete="list"]')
# unit.send_keys('Метр (м)')
# time.sleep(1)
# unit.send_keys(Keys.ENTER)
# time.sleep(1)
#
# """Заполнить объём работ"""
# add_work_plan = driver.find_element(By.XPATH, '//input[@class="clr-col-12 pl-0 ta-c wi-param ng-untouched ng-pristine ng-invalid"]').send_keys('24')
# time.sleep(1)
#
# """Сохранить задание"""
# save_task = driver.find_element(By.XPATH, '//*[@class="btn btn-sm mdl-add-btn"]').click()
# time.sleep(5)
#
# """Отправка наряда на утверждение"""
# approve = driver.find_element(By.XPATH, '//button[@class="btn btn-sm act-btn btn-issue btn-tool ng-star-inserted"]').click()
# time.sleep(5)
