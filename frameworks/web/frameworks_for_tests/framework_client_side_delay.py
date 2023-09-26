import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_client_side_delay = (By.XPATH, '//a[contains(@href, "clientdelay")]')
    button_client_side_delay = (By.XPATH, '//button[contains(@class, "btn-primary")]')
    success_client_side_delay = (By.XPATH, '//p[contains(@class, "success")]')

class FrameworkClientSideDelay(AnyPage):

    @allure.step('Открываем страницу client_side_delay')
    def open_page_client_side_delay(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_client_side_delay)
        # Нажимаем на ссылку
        self.click_element(Locator.url_client_side_delay)
        return self

    @allure.step('Нажимаем на кнопку client_side_delay')
    def click_button_client_side_delay(self):
        # Нажимаем на кнопку
        self.click_element(Locator.button_client_side_delay)

    @allure.step('Ждем пока данные не отобразятся')
    def wait_for_client_data_not_display(self):
        try:
            # Предпологаем что загрузка не должна превышать 16 секунд, если больше то ошибка
            wait = 16
            self.wait_for_item_not_display(Locator.success_client_side_delay, wait)
            return True
        except:
            return False
