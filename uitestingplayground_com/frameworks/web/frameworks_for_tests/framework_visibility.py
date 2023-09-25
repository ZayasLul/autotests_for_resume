import allure
import pytest
from selenium.webdriver.common.by import By

from uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_visibility = (By.XPATH, '//a[contains(@href, "visibility")]')
    button_hide = (By.XPATH, '//button[@id="hideButton"]')
    button_removed = (By.XPATH, '//button[@id="removedButton"]')
    button_zero_width = (By.XPATH, '//button[@id="zeroWidthButton"]')
    button_overlapped = (By.XPATH, '//button[@id="overlappedButton"]')
    button_transparent = (By.XPATH, '//button[@id="transparentButton"]')
    button_invisible = (By.XPATH, '//button[@id="invisibleButton"]')
    button_not_display = (By.XPATH, '//button[@id="notdisplayedButton"]')
    button_off_screen = (By.XPATH, '//button[@id="offscreenButton"]')


class FrameworkVisibility(AnyPage):

    @allure.step('Открываем страницу visibility')
    def open_page_visibility(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_visibility)
        # Нажимаем на ссылку
        self.click_element(Locator.url_visibility)
        return self

    @allure.step('Нажимаем на кнопку "hide"')
    def click_button_hide(self):
        return self.click_element(Locator.button_hide)

    @allure.step('Получаем лист видимых элементов')
    def get_list_visible_elements(self):
        ''' Данный метод предназаначен для получения bool значений видимости элементов на странице '''
        list_xpath = [Locator.button_removed, Locator.button_zero_width, Locator.button_overlapped,
                      Locator.button_transparent, Locator.button_invisible, Locator.button_not_display,
                      Locator.button_off_screen]
        # Выходной массив
        return_list = []
        # Длинна входного массива
        len_list = len(list_xpath)
        for i in range(0, len_list):
            try:
                self.get_visibility_element(list_xpath[i])
                return_list.append(True)
            except:
                return_list.append(False)
        return return_list
