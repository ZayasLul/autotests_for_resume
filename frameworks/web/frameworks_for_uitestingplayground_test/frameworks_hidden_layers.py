import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_hidden_layers = (By.XPATH, '//a[contains(@href, "hiddenlayers")]')
    button_hidden_layers = (By.XPATH, '//button[@id ="greenButton"]')

class FrameworkHiddenLayer(AnyPage):

    @allure.step('Открываем страницу hidden_layers')
    def open_page_hidden_layers(self):
        self.open_page(Locator.url_hidden_layers)
        return self

    @allure.step('Нажимаем на кнопку')
    def click_button_hidden_layers(self):
        # Нажимаем на кнопку на уровне 1
        self.click_element(Locator.button_hidden_layers)
        return self