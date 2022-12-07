import sys
from selene.support.shared import browser
from selenium.webdriver import Keys


def fill_date_of_birthday(date: str):
    name_os = sys.platform
    if name_os == 'darwin':
        browser.element("#dateOfBirthInput").click().send_keys(Keys.COMMAND + 'a').type(date).press_enter()
    else:
        browser.element("#dateOfBirthInput").click().send_keys(Keys.CONTROL + 'a').type(date).press_enter()


def select_date_of_birthday():
    browser.element("#dateOfBirthInput").click()
    month = browser.element(".react-datepicker__month-select").type("January")
    year = browser.element(".react-datepicker__year-select").type("1997")
    browser.element("[aria-label='Choose Saturday, January 25th, 1997']").click()
