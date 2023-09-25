import allure
from selenium.webdriver.common.by import By

from uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_text_input = (By.XPATH, '//a[contains(@href, "textinput")]')
    input_name_button_field = (By.XPATH, '//input[@id="newButtonName"]')
    button_text_input = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkTextInput(AnyPage):

    @allure.step('Открываем страницу text_input')
    def open_page_text_input(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_text_input)
        # Нажимаем на ссылку
        self.click_element(Locator.url_text_input)
        return self

    @allure.step('Вводим имя кнопки')
    def input_name_button(self, new_name_button):
        return self.send_keys(Locator.input_name_button_field, new_name_button)

    @allure.step('Нажимаем на кнопку')
    def click_button_text_input(self):
        # Нажимаем на кнопку
        self.click_element(Locator.button_text_input)

    @allure.step('Получаем имя кнопки')
    def get_name_button(self):
        # Получаем имя кнопки
        return self.get_tag_text(Locator.button_text_input)