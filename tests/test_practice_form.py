from pages.practice_form_page import PracticeFormPage
from textarea.fill_text_area import fill_textarea
import allure


def test_fill_form(driver):
    practice_form_page = PracticeFormPage(driver)
    textarea_value = fill_textarea(driver)
    practice_form_page.fill_form("First", "password", "email@example.com", textarea_value)
    practice_form_page.check_form_submission()