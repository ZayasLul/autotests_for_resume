import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_click = (By.XPATH, '//a[contains(@href, "click")]')
    button_click = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkClick(AnyPage):

    @allure.step('Открываем страницу click')
    def open_page_click(self):
        self.open_page(Locator.url_click)
        return self

    @allure.step('Нажимаем на кнопку @Click@')
    def click_button_click(self):
        try:
            # Нажимаем на кнопку
            self.click_element(Locator.button_click)
            return True
        except:
            return False
