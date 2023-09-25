import allure

from uitestingplayground_com.frameworks.web.any_pages import AnyPage
from selenium.webdriver.common.by import By

class Locator:
    url_dynamic_id = (By.XPATH, '//a[contains(@href, "dynamicid")]')
    button_dynamic_id = (By.XPATH, '//button[contains(@class, "btn-primary")]')

class FrameworkDynamicId(AnyPage):

    @allure.step('Открываем страницу dynamic_id')
    def open_page_dynamic_id(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_dynamic_id)
        # Нажимаем на ссылку
        self.click_element(Locator.url_dynamic_id)
        return self

    @allure.step('ОНажимаем на кнопку с динамическим id')
    def click_button_dynamic_id(self):
        try:
            self.click_element(Locator.button_dynamic_id)
            return True
        except:
            return False
