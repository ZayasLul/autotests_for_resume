import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_non_breaking_space = (By.XPATH, '//a[contains(@href, "nbsp")]')
    button_non_breaking_space = (By.XPATH, '//button[text()="My\u00a0Button"]') # Ставим юникод данного пробела


class FrameworkNoneBreakingSpace(AnyPage):

    @allure.step('Открываем страницу non_breaking_space')
    def open_page_non_breaking_space(self):
        self.open_page(Locator.url_non_breaking_space)
        return self

    @allure.step('Нажимаем на кнопку')
    def click_button_non_breaking_space(self):
        try:
            self.click_element(Locator.button_non_breaking_space)
            return True
        except:
            return False
