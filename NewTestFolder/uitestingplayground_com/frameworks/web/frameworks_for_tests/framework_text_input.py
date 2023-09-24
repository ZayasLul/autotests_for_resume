from selenium.webdriver.common.by import By

from NewTestFolder.uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_text_input = (By.XPATH, '//a[contains(@href, "textinput")]')
    input_name_button_field = (By.XPATH, '//input[@id="newButtonName"]')
    button_text_input = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkTextInput(AnyPage):

    def open_page_text_input(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_text_input)
        # Нажимаем на ссылку
        self.click_element(Locator.url_text_input)
        return self

    def input_name_button(self, new_name_button):
        return self.send_keys(Locator.input_name_button_field, new_name_button)

    def click_button_text_input(self):
        # Нажимаем на кнопку
        self.click_element(Locator.button_text_input)

    def get_name_button(self):
        # Получаем имя кнопки
        return self.get_tag_text(Locator.button_text_input)