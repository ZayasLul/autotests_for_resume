import allure
from selenium.webdriver.common.by import By

from uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_ajax_data = (By.XPATH, '//a[contains(@href, "ajax")]')
    button_triggering_ajax_request = (By.XPATH, '//button[contains(@class, "btn-primary")]')
    success_ajax_data = (By.XPATH, '//p[contains(@class, "success")]')

class FrameworkAjaxData(AnyPage):

    @allure.step('Открываем страницу ajax_data')
    def open_page_ajax_data(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_ajax_data)
        # Нажимаем на ссылку
        self.click_element(Locator.url_ajax_data)
        return self

    @allure.step('Нажимаем на кнопку отправки запроса ajax')
    def click_button_triggering_ajax_request(self):
        # Нажимаем на кнопку
        self.click_element(Locator.button_triggering_ajax_request)

    @allure.step('Ждем пока не отобразится данные ajax')
    def wait_for_ajax_data_not_display(self):
        try:
            # Предпологаем что загрузка не должна превышать 16 секунд, если больше то ошибка
            wait = 16
            self.wait_for_item_not_display(Locator.success_ajax_data, wait)
            return True
        except:
            return False
