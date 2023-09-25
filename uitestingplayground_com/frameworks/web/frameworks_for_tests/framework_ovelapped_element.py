import allure
from selenium.webdriver.common.by import By

from uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_overlapped_element = (By.XPATH, '//a[contains(@href, "overlapped")]')
    input_name_field = (By.XPATH, '//input[@id="name"]')

class FrameworkOverlappedElement(AnyPage):

    @allure.step('Открываем страницу overlapped_element')
    def open_page_overlapped_element(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_overlapped_element)
        # Нажимаем на ссылку
        self.click_element(Locator.url_overlapped_element)
        return self

    @allure.step('Вводим имя')
    def input_name(self, name):
        # Прокручиваем до элемента
        self.scroll_to_element(Locator.input_name_field)
        try:
            # Вводим текст
            self.send_keys(Locator.input_name_field, name)
            return True
        except:
            return False
