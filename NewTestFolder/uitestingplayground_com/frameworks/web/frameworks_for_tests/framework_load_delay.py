from selenium.webdriver.common.by import By

from NewTestFolder.uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_load_delay = (By.XPATH, '//a[contains(@href, "loaddelay")]')
    button_appearing_after_delay = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkLoadDelay(AnyPage):

    def open_page_load_delay(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_load_delay)
        # Нажимаем на ссылку
        self.click_element(Locator.url_load_delay)
        return self

    def click_button_appearing_after_delay(self):
        # Нажимаем на кнопку
        self.click_element(Locator.button_appearing_after_delay)
