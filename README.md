# QA framework
## проект выполнен по тестовому заданию SDET
#### условие задания:
* Открыть браузер
* Перейти по ссылке https://practice-automation.com/form-fields/
  * Шаги:
* Заполнить поле Name
* Заполнить поле Password
* Из списка What is your favorite drink? выбрать Milk и Coffee
* Из списка What is your favorite color? выбрать Yellow
* В поле Do you like automation? выбрать любой вариант
* Поле Email заполнить строкой формата name@example.com
* В поле Message написать количество инструментов, описанных в пункте Automation tools
  * ***дополнительный пункт повышенной сложности***
    * ***В поле Message дополнительно написать инструмент из списка Automation tools, содержащий
наибольшее количество символов***
* Нажать на кнопку Submit
* Ожидаемый результат: Появился алерт с текстом *Message received!*
#
### Проект выполнен на языке ***Python*** ![Python 3.10, 3.11](https://img.shields.io/github/pypi/pyversions/Farkhat1986?color=blueviolet)
### Применены следующие библиотеки 
* *PyTest*
* *Selenium*
* *Allure*
#
# Cтруктура проетка 
 ```
QA/
 │
 ├── github/
 │   └── workflows/
 |      └── run_tests.yml
 ├── tests/
 │   ├── __init__.py
 │   ├── conftest.py
 │   └── test_practice_form.py
 ├── pages/
 │   ├── __init__.py
 │   └── practice_form_page.py
 ├── textarea/
 │   └── fill_text_area.py
 └── requirements.txt
```
#
![Результат отчета](https://github.com/Farkhat1986/QA/blob/master/allure.png)



