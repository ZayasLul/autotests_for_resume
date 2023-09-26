import allure

from frameworks.web.any_pages import AnyPage
from selenium.webdriver.common.by import By

class Locator:
    url_class_attribute = (By.XPATH, '//a[contains(@href, "classattr")]')
    button_blue = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkClassAttribute(AnyPage):

    @allure.step('Открываем страницу class_attribute')
    def open_page_class_attribute(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_class_attribute)
        # Нажимаем на ссылку
        self.click_element(Locator.url_class_attribute)
        return self

    @allure.step('Нажимаем на синюю кнопку')
    def click_button_blue(self):
        # Нажимаем на кнопку
        self.click_element(Locator.button_blue)
