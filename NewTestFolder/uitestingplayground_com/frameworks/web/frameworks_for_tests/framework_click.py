from selenium.webdriver.common.by import By

from NewTestFolder.uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_click = (By.XPATH, '//a[contains(@href, "click")]')
    button_click = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkClick(AnyPage):

    def open_page_click(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_click)
        # Нажимаем на ссылку
        self.click_element(Locator.url_click)
        return self

    def click_button_click(self):
        try:
            # Нажимаем на кнопку
            self.click_element(Locator.button_click)
            return True
        except:
            return False
