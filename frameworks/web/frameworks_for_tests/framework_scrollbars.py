import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_scrollbars = (By.XPATH, '//a[contains(@href, "scrollbars")]')
    button_scrollbars = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkScrollbars(AnyPage):

    @allure.step('Открываем страницу scrollbars')
    def open_page_scrollbars(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_scrollbars)
        # Нажимаем на ссылку
        self.click_element(Locator.url_scrollbars)
        return self

    @allure.step('Нажимаем на кнопку')
    def click_button_scrollbars(self):
        try:
            self.scroll_to_element(Locator.button_scrollbars)
            # Нажимаем на кнопку
            self.click_element(Locator.button_scrollbars)
            return True
        except:
            return False