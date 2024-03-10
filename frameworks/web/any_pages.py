import allure
from selenium.webdriver.common.by import By

from frameworks.web.framework_web_base import FrameworkWebBase

class Locator:
    url_elements = (By.XPATH, '(//div[contains(@class, "avatar")])[1]')

class AnyPage(FrameworkWebBase):

    @allure.step('Открываем страницу')
    def open_page(self, xpath_link):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(xpath_link)
        # Нажимаем на ссылку
        self.click_element(xpath_link)
        return self

    @allure.step('Открываем страницу elements')
    def open_page_elements_demoqa(self):
        self.open_page(Locator.url_elements)
        return self