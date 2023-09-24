from selenium.webdriver.common.by import By

from NewTestFolder.uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_hidden_layers = (By.XPATH, '//a[contains(@href, "hiddenlayers")]')
    button_hidden_layers = (By.XPATH, '//button[@id ="greenButton"]')

class FrameworkHiddenLayer(AnyPage):

    def open_page_hidden_layers(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_hidden_layers)
        # Нажимаем на ссылку
        self.click_element(Locator.url_hidden_layers)
        return self

    def click_button_hidden_layers(self):
        # Нажимаем на кнопку на уровне 1
        self.click_element(Locator.button_hidden_layers)
        return self