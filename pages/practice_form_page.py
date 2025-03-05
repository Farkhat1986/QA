from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure


class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, password, email, fill_textarea):
        with allure.step('Заполнение формы для имени'):
            self.driver.find_element(By.ID, 'name-input').send_keys(first_name)
        with allure.step('Заполнение формы Пароля'):
            self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
        with allure.step('Любимый напиток первый'):
            self.driver.find_element(By.CSS_SELECTOR, "[for='drink2']").click()
        with allure.step('Любимый напиток второй'):
            self.driver.find_element(By.CSS_SELECTOR, "[for='drink3']").click()
        with allure.step('скролим окно'):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)
        with allure.step('Заполняем форму Любимый цвет'):
            self.driver.find_element(By.XPATH, '//input[@id="color3" and @name="fav_color" and @value="Yellow"]').click()
        with allure.step('Выбираем автоматизацию'):
            dropdown = self.driver.find_element(By.ID, 'automation')
            select = Select(dropdown)
            select.select_by_value('yes')
        with allure.step('Заполняем форму почты'):
            self.driver.find_element(By.ID, 'email').send_keys(email)
            time.sleep(1)
        with allure.step('скролим окно второй раз'):
            self.driver.execute_script("window.scrollBy(0, 600);")
        with allure.step('Заполняем форму Textarea с количество инструментов, а так же выбираем инструмент с наибольшим количеством элементов'):
            self.driver.find_element(By.ID, 'message').send_keys(fill_textarea)
            with allure.step('скролим окно'):
                self.driver.execute_script("window.scrollBy(0, 700);")
                time.sleep(1)
        with allure.step('Нажимаем на кнопку для регистрации'):
            self.driver.find_element(By.ID, 'submit-btn').click()


    def check_form_submission(self):
        with allure.step('Ждем появления окна после заполения формы'):
            alert = WebDriverWait(self.driver, 10).until(
                EC.alert_is_present())
            assert alert.text == "Message received!"
            alert.accept()
            time.sleep(5)