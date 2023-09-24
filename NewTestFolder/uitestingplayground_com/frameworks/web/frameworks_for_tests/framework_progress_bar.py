from selenium.webdriver.common.by import By

from NewTestFolder.uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_progress_bar = (By.XPATH, '//a[contains(@href, "progressbar")]')
    button_start = (By.XPATH, '//button[@id="startButton"]')
    button_stop = (By.XPATH, '//button[@id="stopButton"]')
    progress_bar = (By.XPATH, '//div[@id="progressBar"]')
    result_text = (By.XPATH, '//p[@id="result"]')

class FrameworkProgressBar(AnyPage):

    def open_page_progress_bar(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_progress_bar)
        # Нажимаем на ссылку
        self.click_element(Locator.url_progress_bar)
        return self

    def click_start_button(self):
        self.click_element(Locator.button_start)

    def click_stop_button(self):
        self.click_element(Locator.button_stop)

    def click_stop_when_progress_bar_has_reached_value(self):
        value_complete = 75
        while(True):
            value_progress_bar = int(self.get_tag_attribute(Locator.progress_bar, 'aria-valuenow'))
            if value_progress_bar == value_complete:
                self.click_stop_button()
                return self

    def get_result(self):
        return self.get_tag_text(Locator.result_text).split(',')[0]