import pytest
import time
from selenium import webdriver

def test_add_to_busket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_class_name('btn-add-to-basket')
    assert len(button) > 0, "Can't find ADD button!"
