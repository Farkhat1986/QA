import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless=new')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://practice-automation.com/form-fields/")
    yield driver
    driver.quit()


