import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_shadow_dom = (By.XPATH, '//a[contains(@href, "shadowdom")]')
    shadow_host = 'guid-generator'
    shadow_button_generate = 'button[id="buttonGenerate"]'
    shadow_button_copy = 'button[id="buttonCopy"]'
    input_guid_field = 'input[id="editField"]'

class FrameworkShadowDom(AnyPage):

    @allure.step('Открываем страницу shadow_dom')
    def open_page_shadow_dom(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_shadow_dom)
        # Нажимаем на ссылку
        self.click_element(Locator.url_shadow_dom)
        return self

    @allure.step('Нажимаем на кнопку генерации GUID')
    def click_shadow_button_generate(self):
        # Получаем shador-root элемент
        element = self.get_shadow_root_attribute(Locator.shadow_host, Locator.shadow_button_generate)
        element.click()
        return self

    @allure.step('Нажимаем кнопку "Копировать"')
    def click_shadow_button_copy(self):
        # Получаем shador-root элемент
        element = self.get_shadow_root_attribute(Locator.shadow_host, Locator.shadow_button_copy)
        element.click()
        return self

    @allure.step('Получаем значение из поля ввода')
    def get_value_input_field(self):
        # Получаем shador-root элемент
        element = self.get_shadow_root_attribute(Locator.shadow_host, Locator.input_guid_field)
        # Нажимаем на поле
        element.click()
        # Выделяем текст
        element.send_keys(Keys.CONTROL, "a")
        # Копируем в буфер обмена
        element.send_keys(Keys.CONTROL, "c")
        # Получаем значение из буфера обмена
        return self.get_value_in_clipboard()