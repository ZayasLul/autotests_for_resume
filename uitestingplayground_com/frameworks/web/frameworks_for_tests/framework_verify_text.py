import allure
from selenium.webdriver.common.by import By

from uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_verify_text = (By.XPATH, '//a[contains(@href, "verifytext")]')
    find_text = (By.XPATH, '//div[@class="bg-primary"]//span[@class="badge-secondary"]')

class FrameworkVerifyText(AnyPage):

    @allure.step('Открываем страницу verify_text')
    def open_page_verify_text(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_verify_text)
        # Нажимаем на ссылку
        self.click_element(Locator.url_verify_text)
        return self

    @allure.step('Находим и получаем текст')
    def get_and_find_text(self):
        try:
            self.find_element(Locator.find_text)
            return self.get_tag_text(Locator.find_text)
        except:
            return self
