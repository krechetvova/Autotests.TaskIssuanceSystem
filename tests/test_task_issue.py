import time

import pytest

from pages.task_issue import Task
from pages.task_item import TaskItem

"""Книга наряда"""
@pytest.mark.skip
def test_add_taskIssue(test_authorization, driver):
    creat_issue = Task(driver)
    creat_issue.open()
    creat_issue.click_button_delete_taskIssue()
    creat_issue.click_button_delete_yes_taskIssue()
    time.sleep(2)
    creat_issue.click_button_taskIssue()
    time.sleep(2)


"""Карточка задания"""
@pytest.mark.skip
def test_add_taskItem(test_authorization,driver):
    test_add_taskIssue(test_authorization,driver) #создаёт наряд
    task_item = TaskItem(driver)
    task_item.click_button_taskItem()

@pytest.mark.skip
def test_add_worker(test_authorization,driver):
    test_add_taskItem(test_authorization, driver) #создаёт наряд и добавляет карточку задания
    task_item = TaskItem(driver)
    task_item.click_button_worker()
    task_item.send_search_worker()
    time.sleep(2)
    task_item.click_button_save_worker()
    time.sleep(2)
