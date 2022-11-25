from selene import have, Element
from selene.support.shared import browser


class DropDown:
    def __init__(self, element: Element):
        self.element = element

    def select(self, option):
        self.element.click()
        browser.all('[id^=react-select][id*=-option-]').element_by(have.exact_text(option)).click()
