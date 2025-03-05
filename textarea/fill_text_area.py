from selenium.webdriver.common.by import By


def fill_textarea(driver):
    ul_element = driver.find_element(By.ID, 'feedbackForm')
    li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
    items = [li.text for li in li_elements]
    item = items[-1] + " инструмент содержащий наибольшее количество символов, " \
           + str(len(items)) + " " \
           + "количество инструментов в списке"
    return item