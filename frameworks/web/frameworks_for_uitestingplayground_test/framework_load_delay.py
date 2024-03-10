import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_load_delay = (By.XPATH, '//a[contains(@href, "loaddelay")]')
    button_appearing_after_delay = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkLoadDelay(AnyPage):

    @allure.step('Открываем страницу load_delay')
    def open_page_load_delay(self):
        self.open_page(Locator.url_load_delay)
        return self

    @allure.step('Нажимаем на кнопку')
    def click_button_appearing_after_delay(self):
        try:
            # Нажимаем на кнопку
            self.click_element(Locator.button_appearing_after_delay)
            return True
        except:
            return False
