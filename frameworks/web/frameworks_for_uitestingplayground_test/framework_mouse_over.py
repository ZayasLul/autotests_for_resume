import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_mouse_over = (By.XPATH, '//a[contains(@href, "mouseover")]')
    href_click_me = (By.XPATH, '//a[@title="Click me"]')
    href_click_me_active_link = (By.XPATH, '//a[@title="Active Link"]')
    count_click_link = (By.XPATH, '//span[@id="clickCount"]')


class FrameworkMouseOver(AnyPage):

    @allure.step('Открываем страницу sample_app')
    def open_page_sample_app(self):
        self.open_page(Locator.url_mouse_over)
        return self

    @allure.step('Кликаем два раза на кнопку "Click me"')
    def double_click_button_click_me(self):
        # Наводимся на ссылку
        self.move_to_element(Locator.href_click_me)
        # Нажимаем на ссылку 2 раза
        self.click_element(Locator.href_click_me_active_link)
        self.click_element(Locator.href_click_me_active_link)
        return self

    @allure.step('Получаем количество нажатий на кнопку')
    def get_count_click(self):
        return int(self.get_tag_text(Locator.count_click_link))